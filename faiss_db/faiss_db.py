from dotenv import load_dotenv
import os
from langchain.document_loaders import JSONLoader

load_dotenv()

if __name__ == "__main__":
    cohorts_path = "C:/Users/Fedor/Desktop/Python/100PROJECTS/Cohort_Classifier/faiss_db/cohorts.json"
    loader = JSONLoader(
        file_path=cohorts_path,
        jq_schema=".",
    )
    doc = loader.load()