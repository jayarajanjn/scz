from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from contactme.views import ContactView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^contact/$', ContactView.as_view(), name= 'contact'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^markdown/', include('django_markdown.urls')),

]
