# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.template import Library
from django.utils.html import format_html
from django_blog.models import Post
from django_blog.forms import PostForm

register = Library()

@register.simple_tag
def all_posts():
    posts = Post.objects.all()
    return posts 
