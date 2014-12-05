from django.db import models as m
import datetime
from django.utils import timezone

# Create your models here.


class Question(m.Model):
    question_text = m.TextField(max_length=200)
    pub_date = m.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(m.Model):
    question = m.ForeignKey(Question)
    choice_text = m.CharField(max_length=200)
    votes = m.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
