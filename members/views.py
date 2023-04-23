from .forms import SignUpForm, BillingForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.utils import timezone
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and (len(CustomUser.objects.all()) < 1001):
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            if user.pay_online == False:
                return redirect('news')
            else:
                return redirect('members:billing')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class DirectoryView(generic.ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'members/directory.html'

    def get_queryset(self):
        return CustomUser.objects.all().order_by("last_name")

def billing(request, pk):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            user = CustomUser.objects.get(id=pk)
            user.total_due = 0.00  # change field
            user.save() # this will update only
            return render(request, 'members/success.html')
    form = BillingForm()
    context = {'form': form}
    return render(request, 'members/bills.html', context)

def index(request):
    return render(request, 'signup.html', context)