from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CommentForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea)