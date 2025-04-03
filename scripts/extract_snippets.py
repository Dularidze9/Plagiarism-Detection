import glob
from collections import defaultdict
import pygments.lexers

def detect_language(code):
    try:
        lexer = pygments.lexers.guess_lexer(code)
        return lexer.name.lower()
    except:
        return "unknown"

def chunk_code(code, chunk_size=200):
    lines = code.split("\n")
    chunks = []
    current_chunk = []
    for line in lines:
        current_chunk.append(line)
        if len(" ".join(current_chunk)) >= chunk_size:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
    if current_chunk:
        chunks.append("\n".join(current_chunk))
    return chunks

def extract_and_classify_snippets(clone_dir="repos"):
    code_files = glob.glob(f"{clone_dir}/**/*.*", recursive=True)
    classified_snippets = defaultdict(list)
    
    for file in code_files:
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
                lang = detect_language(code)
                chunks = chunk_code(code)
                classified_snippets[lang].extend(chunks)
        except:
            continue
    return classified_snippets
