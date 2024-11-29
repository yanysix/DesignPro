from . import views
from django.urls import re_path
from django.urls import path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('register/', views.sign_up, name='register'),
    path('create_request/', views.create_request, name='create_request'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
]