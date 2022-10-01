
from webapp.models import GuestBook
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import GuestBookForm



def guest_create_view(request, *args, **kwargs):
    form = GuestBookForm()
    if request.method == 'GET':
        return render(request, 'guest_create.html', context={'form': form})
    form = GuestBookForm(request.POST)
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
    
def guest_update_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(initial={
            'author_name': guest.author_name, 
            'author_email': guest.author_email,
            'text':guest.text
        })
        return render(request, 'update.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest.author_name = form.cleaned_data['author_name']
            guest.author_email = form.cleaned_data['author_email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'guest': guest})