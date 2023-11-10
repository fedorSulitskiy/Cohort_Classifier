from fastapi import FastAPI
from llm_agents.llm_agents import CohortQualifier
from news_search.news_search import harvey_helper
app = FastAPI()

CQ = CohortQualifier()

@app.get("/process/")
async def process_input(input_str: str):
    result = CQ.classify(input_str)
    return {"output": result}

@app.get("/harvey/")
async def process_input(input_str: str):
    result = harvey_helper(input_str)
    return {"output": result}

@app.get("/length/")
async def process_input(input_str: str):
    result = CQ.get_website_text(input_str)
    return {"output": len(result)}