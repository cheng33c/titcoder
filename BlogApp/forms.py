
# -*- coding: utf-8 -*-


from django import forms
from .models import Article, BlogComment


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'user_email', 'body']
        widgets = {
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.Textarea(attrs={'placeholder': '我来评两句~'}),
        }

class PublishArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'title':'title', 'placeholder': '文章标题'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'title':'title', 'placeholder': '文章标签'}))
    summary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'title':'title', 'placeholder': '文章摘要'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'title':'title', 'placeholder': '文章内容'}))