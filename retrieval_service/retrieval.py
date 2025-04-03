import faiss
from embeddings_service.embeddings import embed_code
from collections import defaultdict

embedding_dim = 768
language_indexes = {}
retrievers = {}
code_snippets_by_lang = defaultdict(list)

def index_code_snippets(classified_snippets):
    global language_indexes, code_snippets_by_lang, retrievers

    for lang, snippets in classified_snippets.items():
        if lang not in language_indexes:
            language_indexes[lang] = faiss.IndexFlatL2(embedding_dim)
        
        embeddings = embed_code(snippets)
        language_indexes[lang].add(embeddings)
        code_snippets_by_lang[lang].extend(snippets)
        retrievers[lang] = language_indexes[lang]
