from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import Username
from django.contrib import messages

# Create your views here.
def index(request):
    if request.front_user:
        print(request.front_user.username)
    return render(request, "index.html")

def python(request):
    if request.front_user:
        print(request.front_user.username)
    return render(request, "python.html")

class Sign_in(View):
    def get(self, request):
        return render(request, "sign_in.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        Username.objects.create(username=username, password=password)
        exit = Username.objects.filter(username=username, password=password).first()
        if exit:
            request.session["user_id"] = exit.id
            request.session.set_expiry(0)
            return redirect(reverse("front:index"))
        else:
            messages.info(request, "用户名或者密码错误")
            redirect(reverse("front:sign_in"))