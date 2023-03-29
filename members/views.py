from django.shortcuts import render
from .forms import MembersForm

def members_view(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'members/success.html')
    form = MembersForm()
    context = {'form': form}
    return render(request, 'members/members.html', context)

