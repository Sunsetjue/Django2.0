from django.shortcuts import render
from .django_form import MessageBoardForm,Forms,RegisteredForm
from django.views.generic import View
from django.http import HttpResponse
from django.forms.utils import ErrorDict
from .models import Registered
# Create your views here.
class One(View):
    def get(self,request):
        form = MessageBoardForm()
        return render(request, "one.html", context={"form": form})

    def post(self, request):
        msg = MessageBoardForm(request.POST)
        if msg.is_valid(): # 如果验证成功
            title = msg.cleaned_data.get("title")
            content = msg.cleaned_data.get("content")
            email = msg.cleaned_data.get("email")
            reply = msg.cleaned_data.get("reply")
            dict = {"dict":{
                "title": title,
                "content": content,
                "email": email,
                "reply": reply
            }}
            return render(request, "two.html", context=dict)
        else:
            print(msg.errors.get_json_data())
            return HttpResponse("fail")

class Two(View):
    def get(self, request):
        return render(request, "three.html")

    def post(self, request):
        forms = Forms(request.POST)
        if forms.is_valid():
            return HttpResponse("success")
        else:
            print(forms.errors.get_json_data())
            return HttpResponse("fail")

class Three(View):
    def get(self, request):
        return render(request, "registered.html")

    def post(self, request):
        form = RegisteredForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            telephone = form.cleaned_data.get("telephone")
            Registered.objects.create(name=name, telephone=telephone)
            return HttpResponse("注册成功")
        else:
            print(form.get__error())
            return HttpResponse("注册失败")
