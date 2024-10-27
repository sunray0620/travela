from django.http import HttpResponse
from django.shortcuts import render

from audiointro.libs.audio_intro_retriever import get_audio_intro

def index(request):
    test_audio_intro = get_audio_intro()
    return HttpResponse(test_audio_intro)