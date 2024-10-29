'''
The module that contains the audio intro views.
'''
import json
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from audiointro.libs.audio_intro_retriever import AudioIntroRetriever
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient


def index(request):
    '''index view.'''
    prompt = request.GET.get('prompt', None)
    if not prompt:
        return JsonResponse({'content': 'error: cannot find prompt.'})

    generativelanguage_client = GenerativeLanguageClient()
    audio_intro_retriever = AudioIntroRetriever(generativelanguage_client)
    gemini_response = audio_intro_retriever.get_audio_intro(prompt)
    response = {
        'content': gemini_response
    }

    return JsonResponse(response)


@csrf_exempt  # Use this only if you're testing locally and don’t want to handle CSRF tokens.
def audio_intro(request):
    '''Post method to retrieve audio intro'''
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        return render(request, 'audiointro/get_audio_intro.html')

    # Handle the POST request here
    data = json.loads(request.body)
    query = data.get('query', '')

    res = {
        'query': query,
        'result_text': 'result_text',
        'result_audio': 'result_audio',
    }
    return JsonResponse(res)
