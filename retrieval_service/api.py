from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import retrievers, code_snippets_by_lang
from embeddings_service.embeddings import embed_code

app = FastAPI()

class CodeQuery(BaseModel):
    code_snippet: str

@app.post("/retrieve")
def retrieve_similar_code(query: CodeQuery):
    query_embedding = embed_code([query.code_snippet])
    lang = detect_language(query.code_snippet)
    
    if lang not in retrievers:
        return {"error": "No indexed code for this language"}
    
    D, I = retrievers[lang].search(query_embedding, k=5)
    return {"similar_code": [code_snippets_by_lang[lang][idx] for idx in I[0]]}
