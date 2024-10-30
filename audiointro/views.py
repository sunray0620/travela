'''
The module that contains the audio intro views.
'''
import json
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

from audiointro.libs.audio_intro_retriever import AudioIntroRetriever
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient
from shared.gcloud_client.texttospeech_client import TextToSpeechClient

def audio_intro(request):
    '''Post method to retrieve audio intro'''
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        return render(request, 'audiointro/get_audio_intro.html')

    # Handle the POST request here
    data = json.loads(request.body)
    print(f'data: {data}')
    query = data.get('query', '')
    print(f'query: {query}')

    generativelanguage_client = GenerativeLanguageClient()
    texttospeech_client = TextToSpeechClient()
    audio_intro_retriever = AudioIntroRetriever(generativelanguage_client, texttospeech_client)
    resp = audio_intro_retriever.get_audio_intro(query)
    return JsonResponse(resp)
