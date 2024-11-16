'''
The module that controls the url patterns.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.audio_intro, name='audio_intro'),
    path('download_audio', views.download_audio, name='download_audio'),
    path('download_gcs_blob', views.download_gcs_blob, name='download_gcs_blob'),
]
