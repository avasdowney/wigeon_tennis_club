from django.http import HttpResponse

def index(request):
    return HttpResponse("")

def login(request):
    return HttpResponse("User Login")

def create_account(request):
    return HttpResponse("Create Account")

def news(request):
    return HttpResponse("News")

def directory(request):
    return HttpResponse("Directory")

def member_profile(request):
    return HttpResponse("Member Profile")

def admin_dashboard(request):
    return HttpResponse("Admin Profile")

def treasurer_dashboard(request):
    return HttpResponse("Treasurer Profile")

def payment(request):
    return HttpResponse("Payment")

def reserve_court(request):
    return HttpResponse("Reserve Court")