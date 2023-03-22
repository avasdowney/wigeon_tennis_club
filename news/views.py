from django.shortcuts import render
from .forms import NewsForm


def news_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/success.html')
    form = NewsForm()
    context = {'form': form}
    return render(request, 'news/news.html', context)
