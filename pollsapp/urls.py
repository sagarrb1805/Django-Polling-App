from django.urls import path
from django.utils.regex_helper import normalize
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('vote/<questionid>/', views.vote, name='vote'),
    path('result/<questionid>', views.result, name='result'),
]