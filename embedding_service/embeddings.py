import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

# Load CodeBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

def embed_code(snippets):
    inputs = tokenizer(snippets, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state[:, 0, :]
    return embeddings.numpy()
