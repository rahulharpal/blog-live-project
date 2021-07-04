from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.forms import CommentForm
from datetime import date
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None    
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/postlist.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            print('hello')
            new_comment=form.save(commit=False)
            print('hello')
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'blog/postdetail.html',{'post':post,'form':form,'comments':comments,'csubmit':csubmit})

from django.core.mail import send_mail
from blog.forms import Emailsendform

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    form=Emailsendform()
    sent=False
    print('hello')
    if request.method=='POST':
        mail=Emailsendform(request.POST)
        if mail.is_valid():
            cd=mail.cleaned_data
            send_mail('Subject',"Here is the message",'rahulkumar.harpal2022@gmail.com',['rahulkumar.pal2031@gmail.com'],fail_silently=False,)
    return render(request,'blog/sharebymail.html',{'form':form,'post':post})
