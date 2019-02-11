from .models import Username

# 自定义中间件

def front_middlewares(get_response):
    print("在程序启动的时候就会执行的语句")
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

# 用类的方式表达
class FrontMiddlewares(object):
    def __init__(self, get_response):
        print("在程序启动的时候就会执行的语句")
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = Username.objects.get(id=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = self.get_response(request)