from fastapi import FastAPI
from pydantic import BaseModel
from embeddings import embed_code

app = FastAPI()

class CodeSnippet(BaseModel):
    code: str

@app.post("/embed")
def generate_embedding(snippet: CodeSnippet):
    return {"embedding": embed_code([snippet.code]).tolist()}
