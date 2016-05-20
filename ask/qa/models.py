from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.http import Http404

class Question(models.Model):
    object=QuestionManager()
	title=models.CharField(max_length=200)
	text=models.TextField()
	added_at=models.DateTimeField()
	rating=models.SmallIntegerField()    
	author=models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            null=True,
                            related_name='+')
	likes=models.ManyToManyField(User,
                            related_name='+')

class Answer(models.Model):
    text=models.TextField()
    added_at=models.DateTimeField()
    question=models.OneToOneField(Question)
    author=models.OneToOneField(User,
                                related_name='+')

def paginate(request,qs):
    try:
        limut=int(request.GET.get('limit',10))
    except ValueError:
        limit=10
    if limit>100:
        limit=10
    try:
        page=int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    paginator=Paginator(qs,limit)
    try:
        page=paginator.page(page)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    return page