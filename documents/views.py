from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import TemplateView


#def index(request):
#      return HttpResponse("Hello, world. You're at the documents views.py.")

class DocumentsView(TemplateView):
    template_name = "documents.html"
