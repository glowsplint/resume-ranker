from typing import List
from itertools import chain
from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from resumeranker.ranker import Document, Relevance, extract_docx, extract_pdf

app = FastAPI()

# Mounting static files
app.mount(
    '/static', StaticFiles(directory='./vue-frontend/dist/static'), name='static')
templates = Jinja2Templates(directory='./vue-frontend/dist')

# Furnishing index.html
@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/upload/')
async def process(inputPhrases: str = Form(...), files: List[UploadFile] = File(...)):
    input_phrases = inputPhrases.split('\n')
    docx_list = [
        item for item in files if item.filename.endswith('.docx')]
    pdf_list = [item for item in files if item.filename.endswith('.pdf')]
    for item in chain(docx_list, pdf_list):
        setattr(item.file, 'filename', item.filename)
    docx_doc_list = [Document(item.file, extract_docx, input_phrases)
                     for item in docx_list]
    pdf_doc_list = [Document(item.file, extract_pdf, input_phrases)
                    for item in pdf_list]
    docx_doc_list.extend(pdf_doc_list)
    relevance = Relevance(docx_doc_list)
    print(relevance.scores)
    return relevance.scores
