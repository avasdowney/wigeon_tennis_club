from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .forms import AddNewsForm
from .models import AddNews

def add_news_view(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/success.html')
    form = AddNewsForm()
    context = {'form': form}
    return render(request, 'news/add_news.html', context)

class NewsView(generic.ListView):
    model = AddNews
    context_object_name = 'news_list'
    template_name = 'news/news_home.html'

    def get_queryset(self):
        return AddNews.objects.all().order_by("-date")
