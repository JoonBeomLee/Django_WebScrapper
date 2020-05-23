from django.shortcuts import render, redirect
from django import forms

# view home
def index(request):
    return render(request, 'index.html')


# view search
def search_job(request):
    key_word = request.GET.get('search_word')
    context = {"key_word": key_word}
    return render(request, "search.html", context)