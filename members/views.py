from django.shortcuts import render
from .forms import MembersForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "members/signup.html"

def index(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'members/success.html')
    form = MembersForm()
    context = {'form': form}
    return render(request, 'members/members.html', context)

