from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .form import SignUpView,SignInView
from .models import Username,Photo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

class SignIn(View):
    def get(self, request):
        return render(request, "sign_in.html")
    def post(self, request):
        form = SignInView(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            exist = Username.objects.filter(username=username, password=password).first()
            if exist:
                request.session["user_id"] = exist.id
                request.session.set_expiry(0)
                return redirect(reverse("front:index"))
            else:
                messages.info(request, "用户名或者密码错误")
                return redirect(reverse("front:sign_in"))
        else:
            errors = form.get_errors()
            print(form.errors.get_json_data())
            for error in errors:
                messages.info(request, error)
            return redirect(reverse("front:sign_in"))

class SignUp(View):
    def get(self, request):
        return render(request, "sign_up.html")
    def post(self, request):
        form = SignUpView(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data.get("pwd1")
            user.save()
            return redirect(reverse("front:sign_in"))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            for error in errors:
                messages.info(request, error)
            return redirect(reverse("front:sign_up"))

def python(request):
    return render(request, "python.html")

def django(request):
    return render(request, "django.html")

class CutPhoto(View):
    def get(self, request):
        return render(request, "cut_photo.html")
    def post(self, request):
        photo = request.FILES.get("photo")
        Photo.objects.create(photo=photo)
        return redirect(reverse("front:index"))