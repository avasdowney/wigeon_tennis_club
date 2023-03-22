from django.shortcuts import render
from .forms import AddNewsForm


def add_news_view(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/success.html')
    form = AddNewsForm()
    context = {'form': form}
    return render(request, 'news/add_news.html', context)

def news_view(request):
    return render(request, 'news/news_home.html')
