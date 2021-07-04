from django import forms

class Emailsendform(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    to=forms.CharField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

from blog.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
