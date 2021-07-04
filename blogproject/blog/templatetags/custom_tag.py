from django import template
from blog.models import Post
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()
@register.inclusion_tag('blog/latest_post.html')
def show_latest_post(count=4):
    latest_post= Post.objects.all().order_by('-publish')[:count]
    return {'latest_post':latest_post}

from django.db.models import Count
@register.simple_tag
def get_most_commented_post(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
