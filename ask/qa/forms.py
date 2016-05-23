from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer
from datetime import datetime

class AskForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self._user=None
        super(AskForm, self).__init__(*args,**kwargs)

    title=forms.CharField(max_length=80)
    text=forms.CharField(widget=forms.Textarea)

    def save(self):
        question=Question(**self.cleaned_data)
        question.added_at=datetime.now()
        question.rating=0
        question.author=self._user
        question.save()
        return question

class AnswerForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self._user=None
        super(AnswerForm, self).__init__(*args,**kwargs)

    text=forms.CharField(widget=forms.Textarea)
    question=forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        answer=Answer()
        answer.text=self.cleaned_data['text']
        answer.question_id=self.cleaned_data['question']
        answer.added_at=datetime.now()
        answer.author=self._user
        answer.save()
        return answer

class SignupForm(forms.Form):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()

    def clean(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
            raise ValueError

    def save(self):
        user=User.objects.create_user(username=self.cleaned_data['username'],
                                 password=self.cleaned_data['password1'],
                                 email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user