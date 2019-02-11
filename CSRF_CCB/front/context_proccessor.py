from .models import Username

def front_username(request):
    user = request.front_user
    context = {}
    if user:
        try:
            context["front_username"] = user.username
        except:
            pass
    return context

def extra_money(request):
    user = request.front_user
    context = {}
    if user:
        try:
            context["extra_money"] = user.money
        except:
            pass
    return context