from django.shortcuts import render
from webapp.models import GuestBook

def index_view(request):
    guests = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'guests': guests
    }
    return render(request, 'index.html', context)