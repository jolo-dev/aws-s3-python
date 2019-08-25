from django.urls import path

from . import views

app_name = 'listS3Documents'
urlpatterns = [
    path('', views.index, name='index'),
]