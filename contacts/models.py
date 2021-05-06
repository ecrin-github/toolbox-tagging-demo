from django.db import models
from django.conf import settings

from users_management.models import User


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Email subjects'


class Outbox(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, unique=False, related_name='sender')
    receivers = models.ManyToManyField(User, unique=False)
    subject = models.ForeignKey(Subject, unique=False, null=False, blank=False, on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject.name

    class Meta:
        verbose_name_plural = 'Outbox'


class Inbox(models.Model):
    outbox = models.ForeignKey(Outbox, unique=False, on_delete=models.CASCADE)


    def __str__(self):
        return self.outbox.subject.name

    class Meta:
        verbose_name_plural = 'Inbox'
