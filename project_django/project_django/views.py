from django.shortcuts import render

# view home
def index(request):
    return render(request, 'index.html')