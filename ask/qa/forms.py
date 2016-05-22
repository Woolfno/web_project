from django import forms
from qa.models import Question, Answer
from datetime import datetime

class AskForm(forms.Form):
    title=forms.CharField(max_length=80)
    text=forms.CharField(widget=forms.Textarea)

    def save(self):
        question=Question(**self.cleaned_data)
        question.added_at=datetime.now()
        question.rating=0
        question.save()
        return question

class AnswerForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)
    question=forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        answer=Answer()
        answer.text=self.cleaned_data['text']
        answer.question_id=self.cleaned_data['question']
        answer.added_at=datetime.now()
        answer.save()
        return answer