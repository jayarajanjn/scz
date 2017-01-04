from __future__ import unicode_literals
from django.db import models
from django_markdown.models import MarkdownField


class ArticleQuerySet(models.QuerySet):
    def deployed(self):
        return self.filter(deploy=True)

    def drafts(self):
        return self.filter(deploy=False)


class Article(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Title',
                             name='title'
                             )
    content = MarkdownField(verbose_name='Content',
                            name='content',
                            help_text='Add the content of Article here',
                            )
    slug = models.SlugField(max_length=50, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    deploy = models.BooleanField(default=False,
                                 verbose_name='Deployed',
                                 name='deploy',
                                 )
    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return "{title}\n{content}".format(title=self.title,
                                           content=self.content
                                           )

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-create_date"]
