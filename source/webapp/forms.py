from django.forms import ModelForm
from webapp.models import GuestBook
from django.utils.translation import gettext_lazy as _


class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBook
        fields = ('author_name', 'author_email', 'text')
        labels = {
            'author_name': _('Имя'),
            'author_email': _('Email'),
           'text': _('Текст')
        }
        
        