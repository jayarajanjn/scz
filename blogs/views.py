from django.shortcuts import render
from django.views import generic
from .models import Article



class ArticlesListView(generic.ListView):
    model = Article
    template_name = "blogs/index.html"

    def get_queryset(self):
        return Article.objects.filter(deploy=True)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "blogs/blog.html"
