from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    """docstring for Article."""
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thum = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse( 'atricles:edit', args=(post_id, ))

    def snippet(self):
        return self.body[:50]+'.....'
