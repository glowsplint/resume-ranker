from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dragdropapi.ranker import Document, Relevance, extract_docx, extract_pdf


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name


@api_view(['POST'])
def upload(request):
    if request.method == 'POST':
        input_phrases = request.POST.get('inputPhrases').split('\n')
        uploaded_files = request.FILES.getlist('files')

        docx_list = [item for item in uploaded_files if item.name.endswith(
            '.docx')]
        pdf_list = [
            item for item in uploaded_files if item.name.endswith('.pdf')]
        docx_doc_list = [
            Document(item, extract_docx, input_phrases) for item in docx_list]
        pdf_doc_list = [
            Document(item, extract_pdf, input_phrases) for item in pdf_list]
        relevance = Relevance()
        if len(docx_doc_list):
            relevance.add(docx_doc_list)
        if len(pdf_doc_list):
            relevance.add(pdf_doc_list)
        server_response = relevance.scores

    return Response(data=server_response)
