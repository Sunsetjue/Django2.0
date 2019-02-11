from .models import Username

def front_middleware(get_response):
    def middleware(request):
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = Username.objects.get(id=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = get_response(request)
        return response
    return middleware