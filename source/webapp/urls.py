
from django.urls import path
from webapp.views.base import index_view
from webapp.views.guest import guest_create_view, guest_delete_view


urlpatterns= [
    path("", index_view, name='index'),
    path('guest/create', guest_create_view, name='guest_create'),
    path('guest/<int:pk>/delete', guest_delete_view, name='guest_delete')
]