from django.shortcuts import render
from django.views.generic import ListView, DetailView
from newspaper import models


# Create your views here.
def home(request):
    return render(request, 'newspaper/home.html')



class ArticleListView(ListView):
    model = models.Article
    template_name = 'newspaper/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('test', None):
            context['test'] = self.kwargs.get('test')
        return context
