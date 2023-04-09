from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('news')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'members/success.html')
    form = MembersForm()
    context = {'form': form}
    return render(request, 'members/members.html', context)