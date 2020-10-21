from django.shortcuts import render
from . models import Usuario
from django.views import generic

def index(request):

    return render(
        request,
        'index.html',
    )


