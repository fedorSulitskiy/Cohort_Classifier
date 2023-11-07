from fastapi import FastAPI
from smarts.smarts import CohortQualifier
app = FastAPI()

CQ = CohortQualifier()

@app.get("/process/")
async def process_input(input_str: str):
    result = CQ.classify(input_str)
    return {"output": result}
