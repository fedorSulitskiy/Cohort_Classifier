from fastapi import FastAPI
from llm_agents.llm_agents import CohortQualifier

app = FastAPI()

CQ = CohortQualifier()


def description_path(desc: str):
    desc_words = desc.split()

    if len(desc_words) < 50:
        return {
            "result": {"result": "N/A"},
            "source": "source",
            "total_cost": "",
        }

    return CQ.scemantic_classify(desc, "desc")


@app.get("/process/")
async def process_input(desc: str, website: str):
    if " " in website:
        inter = website.split()
        website = inter[0]

    web_text = CQ.get_website_text(website)

    if web_text[:5] == "Error" or len(web_text) < 500:
        return description_path(desc)

    return CQ.scemantic_classify(web_text[:2000], "web")


@app.get("/length/")
async def process_input(input_str: str):
    result = CQ.get_website_text(input_str)
    return {"output": len(result)}
