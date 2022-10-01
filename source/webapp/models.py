from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class GuestBook(models.Model):
    author_name = models.CharField(verbose_name='Имя автора', max_length=30, blank=False, null=False)
    author_email = models.EmailField(verbose_name='Почта автора', max_length=30, blank=False, null=False)
    text = models.TextField(verbose_name='Текст', max_length=400, blank=False, null=False)
    status = models.CharField(verbose_name='Статус', max_length=100, blank=False, null=False, default='active')
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата создания',auto_now=True)
    