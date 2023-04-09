from .forms import SignUpForm
from django.shortcuts import render

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'phone': user.profile.phone},)
 
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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'members/success.html')
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'members/signup.html', context)