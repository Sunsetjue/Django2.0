from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Book

# Create your views here.
class One(View):
    def get(self, request):
        return render(request, 'one.html')

    def post(self, request):
        files = request.FILES.get("get_file")
        with open("my_flies.txt", 'wb') as fp:
            for chunks in files.chunks():
                fp.write(chunks)
        return HttpResponse("success")

class Two(View):
    def get(self, request):
        return render(request, "two.html")

    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        files = request.FILES.get("on_load")
        Book.objects.create(title=title, content=content, on_load=files)
        return HttpResponse("success")