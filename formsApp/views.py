from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.http import HttpRequest
from . forms import ContactForm, SnippetForm
from . models import Snippet

def home(request):

    contex = {
        'key': 'value',
    }
    #return render(request, 'home.html', contex)

def contact(request):
    form = ContactForm(request.POST)
    contex = {
        'key': 'value',
        'form' : form,

    }
    return render(request, 'form.html', contex)

def snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect(snippet)

        
    
    form = SnippetForm()
    contex = {
        'key': 'value',
        'form' : form,

    }
    return render(request, 'form.html', contex)

def out(request):
    if request.method == 'POST':
        return redirect(out)
    all_visitor = Snippet.objects.all
    contex = {
        'key': 'value',
        'all_visitor': all_visitor,

    }
    return render(request, 'out.html', contex)