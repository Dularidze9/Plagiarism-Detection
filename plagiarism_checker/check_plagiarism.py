from fastapi import FastAPI
from pydantic import BaseModel
from retrieval_service.api import retrieve_similar_code
from langchain.llms import OpenAI

app = FastAPI()

class CodeQuery(BaseModel):
    code_snippet: str

@app.post("/check_plagiarism")
def check_plagiarism(query: CodeQuery):
    retrieved_results = retrieve_similar_code(query)
    prompt = f"Is this code plagiarized?\nUser Code:\n{query.code_snippet}\nRetrieved Code:\n" + "\n".join(retrieved_results["similar_code"])

    llm = OpenAI()
    response = llm(prompt)
    plagiarism_status = "Yes" if "yes" in response.lower() else "No"
    
    return {"plagiarism_status": plagiarism_status, "similar_code": retrieved_results["similar_code"]}
