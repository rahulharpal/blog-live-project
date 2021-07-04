from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','Created','Updated','status']
    list_filter=('status','author','Created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','name','email','body','created','updated','active')
    list_filter=('post','name','active')
    search_fields=('post','name','body')
    ordering=['post','created']

admin.site.register(Comment,CommentAdmin)
