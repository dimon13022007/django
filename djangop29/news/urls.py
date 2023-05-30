from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('tasks', views.tasks, name='tasks'),
    path('create', views.create, name='create'),


]





