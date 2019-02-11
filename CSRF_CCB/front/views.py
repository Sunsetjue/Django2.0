from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .form import SignUpForm,SignInForm,TransformForm
from django.contrib import messages
from .models import Username
from django.db.models import F
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from .decorators import front_transform

# Create your views here.
def index(request):
    return render(request, "index.html")

class SignIn(View):
    def get(self, request):
        return render(request, "sign_in.html")
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            password = form.cleaned_data.get("password")
            exit = Username.objects.filter(telephone=telephone, password=password).first()
            if exit:
                request.session["user_id"] = exit.id
                request.session.set_expiry(0)
                return redirect(reverse("front:index"))
            else:
                messages.info(request, "电话号码或者密码错误！")
                return redirect(reverse("front:sign_in"))
        else:
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
                return redirect(reverse("front:sign_in"))
class SignUp(View):
    def get(self, request):
        return render(request, "sign_up.html")
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data.get("pwd1")
            user.save()
            return redirect(reverse("front:sign_in"))
        else:
            print(form.errors.get_json_data())
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse("front:sign_up"))
@method_decorator(decorator=front_transform, name="dispatch")
class Transform(View):
    def get(self, request):
         return render(request, "transform.html")
    def post(self, request):
        form = TransformForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            user_id = request.session.get("user_id")
            count = form.cleaned_data.get("money")
            user = request.front_user
            if user.money >= count:
                Username.objects.filter(telephone=telephone).update(money=F("money")+count)
                user.money -= count
                user.save()
                return render(request, "return-back1.html")
            else:
                return HttpResponse("您的余额不足！")
        else:
            print(form.errors.get_json_data())
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse("front:transform"))

def logout(request):
    request.session.flush()
    return redirect(reverse("front:index"))

@method_decorator(decorator=front_transform, name='dispatch')
class ExtraMoney(View):
    def get(self, request):
        return render(request, "extra_money.html")