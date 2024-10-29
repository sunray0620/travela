'''
The module that controls the url patterns.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.audio_intro, name='audio_intro'),
    path('index', views.index, name='index'),
]
