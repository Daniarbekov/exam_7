from django.contrib import admin
from webapp.models import GuestBook
# Register your models here.



class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id','author_name','author_email','text','status', 'created_at', 'changed_at')
    list_filter = ('id','author_name','author_email','text','status', 'created_at', 'changed_at')
    search_fields = ['status']
    fields = ('id','author_name','author_email','text','status')
    readonly_fields = ('id','created_at')

admin.site.register(GuestBook, GuestBookAdmin)