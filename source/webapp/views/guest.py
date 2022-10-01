
from webapp.models import GuestBook
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import AuthorForm



def guest_create_view(request, *args, **kwargs):
    form = AuthorForm()
    if request.method == 'GET':
        return render(request, 'guest_create.html', context={'form': form})
    form = AuthorForm(request.POST)
    if not form.is_valid():    
        return render(request, 'guest_create.html', context={'form': form})
    guest = GuestBook.objects.create(**form.cleaned_data)        
    if request.method =='POST':
        return redirect('index')
    
def guest_delete_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')