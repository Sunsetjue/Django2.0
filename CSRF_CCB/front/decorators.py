from .models import Username
from django.shortcuts import redirect,reverse

def front_transform(func):
    def wrapper(request, *args, **kwargs):
        if request.front_user:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse("front:sign_in"))
    return wrapper