from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Entry(models.Model):
    '''学习到某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        t = self.text
        if len(self.text) > 50:
            t = f'{self.text[:50]}...'
        return t