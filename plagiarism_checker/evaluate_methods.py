from retrieval_service.api import retrieve_similar_code
from langchain.llms import OpenAI

def evaluate_rag_only(code_snippet):
    return {"rag_similar_code": retrieve_similar_code({"code_snippet": code_snippet})}

def evaluate_llm_only(code_snippet):
    llm = OpenAI()
    response = llm(f"Is this code plagiarized?\n{code_snippet}")
    return {"llm_assessment": response}

def evaluate_full_system(code_snippet):
    return {"rag": evaluate_rag_only(code_snippet), "llm": evaluate_llm_only(code_snippet)}
