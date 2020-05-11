from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name
