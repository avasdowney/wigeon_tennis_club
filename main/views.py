from django.http import HttpResponse


def index(request):
    return HttpResponse("Login Page")

def login(request):
    return HttpResponse("UserLogin")