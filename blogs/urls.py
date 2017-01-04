from django.conf.urls import include, url
from .views import ArticlesListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticlesListView.as_view(), name='blogs'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='blog')
]
