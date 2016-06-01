# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer, Profile
from datetime import datetime
from django.conf import settings


class AskForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self._user = None
        super(AskForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length=80,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Вопрос', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save(self):
        question = Question(**self.cleaned_data)
        question.added_at = datetime.now()
        question.rating = 0
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self._user = None
        super(AnswerForm, self).__init__(*args, **kwargs)

    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введи ваш ответ'}))
    question = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.question_id = self.cleaned_data['question']
        answer.added_at = datetime.now()
        answer.author = self._user
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        try:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise ValueError
        except KeyError:
            raise ValueError

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password1'],
                                        email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password1'])
        profile=Profile.objects.create(user=user)
        profile.avatar=settings.STATIC_URL+'img/not_avatar.png'
        profile.save()
        user.save()
        return user


class ProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self._user = None
        super(ProfileForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nick_name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=False)

    def save(self):
        profile = Profile.objects.get(user=self._user)

        if self.cleaned_data.get('username') is not None and profile.user.username != self.cleaned_data['username']:
            profile.user.username = self.cleaned_data['username']

        if self.cleaned_data.get('email') is not None and profile.user.email != self.cleaned_data['email']:
            profile.user.email = self.cleaned_data['email']

        if self.cleaned_data.get('password') is not None:
            profile.user.set_password(self.cleaned_data['password'])

        if self.cleaned_data.get('nick_name') is not None and profile.nick_name != self.cleaned_data['nick_name']:
            profile.nick_name = self.cleaned_data['nick_name']

        if self.cleaned_data.get('avatar') is not None and profile.avatar != self.cleaned_data['avatar']:
            profile.avatar = self.cleaned_data['avatar']

        profile.save()
        return profile

