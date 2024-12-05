from django.contrib import admin
from django.urls import include, path
from tasks import views

urlpatterns = [
    path('', views.get_all_tasks, name="get_all_tasks"),
]