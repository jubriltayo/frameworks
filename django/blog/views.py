from django.shortcuts import render, get_object_or_404
from django.urls import reverse 

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

# CLASS BASED VIEWS
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    # success_url = '/'  # to overide success redirection

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        """get object by id in kwargs instance"""
        """ this only became necessary because we are using a 
        class based view as function hence the id, pk, slug issue
        """
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        """get object by id in kwargs instance"""
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # queryset = Article.objects.all()
    # success_url = '/blog/'

    def get_object(self):
        """get object by id in kwargs instance"""
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('articles:article-list')