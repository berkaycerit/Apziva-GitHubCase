
from django.contrib import admin
from django.urls import path
from github import views

urlpatterns = [
    path('admin/', admin.site.urls), # admin: berkay cerit | password: 12345678
    path('', views.post_search, name='post_search'),
]
