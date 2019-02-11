from django.shortcuts import render

# Create your views here.
def index_index(request):
    return render(request,"6.html")

def school(request):
    return render(request, "7.html")

def company(request):
    return render(request, "8.html")

def index(request):
    return render(request, "9.html")