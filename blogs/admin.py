from django.contrib import admin
from models import Article
from django_markdown.admin import MarkdownModelAdmin


class ArticleAdmin(MarkdownModelAdmin):
    list_display = ('title', 'create_date', 'deploy')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
