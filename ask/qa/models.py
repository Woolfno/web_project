from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
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