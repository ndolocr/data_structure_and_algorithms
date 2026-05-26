from django.urls import path

from linked_list import views

urlpatterns = [
    path('', views.view_linked_list, name='view_linked_list'),
]