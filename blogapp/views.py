from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


def index_view(request):
    return render(request, 'index.html')
