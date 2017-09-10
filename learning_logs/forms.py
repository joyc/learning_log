#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/9/10 10:41
# @Author  : Hython.com
# @File    : forms.py
# @IDE     : PyCharm

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}