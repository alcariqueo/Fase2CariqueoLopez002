from django.shortcuts import render
from . models import Usuario
from django.views import generic
<<<<<<< HEAD
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse

def index(request):

    return render(
        request,
        'index.html',
    )

class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['email', 'fechaN', 'telefono', 'password']

class UsuarioDelete(DeleteView):
    model = Usuario
    def get_success_url(self):
        return reverse('index')


class UsuarioDetailView(generic.DetailView):
    model=Usuario
=======

def index(request):

    return render(
        request,
        'index.html',
    )


>>>>>>> f0a3373852944327dde91fd3c481cbd19cc5a3a0
