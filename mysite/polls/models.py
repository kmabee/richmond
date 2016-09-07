from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text   = models.CharField(max_length=200)
    pub_date        = models.DateTimeField('date published', auto_now=True)
    total_votes     = models.IntegerField(default=0)
    last_voted      = models.DateTimeField(auto_now=True)
    active          = models.BooleanField(default=True)
    def __str__(self):
        return self.question_text

    # Published in the last 24 hours?
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question        = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text     = models.CharField(max_length=200)
    votes           = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

