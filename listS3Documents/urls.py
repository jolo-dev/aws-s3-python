from django.urls import path

from . import views

app_name = 'listS3Documents'
urlpatterns = [
    path('', views.index, name='index'),
    path('bucket/<str:bucketname>', views.bucketContent, name='first-level'),
    path('<str:bucketname>/<str:path>/', views.bucketContent, name='bucket-detail'),
]