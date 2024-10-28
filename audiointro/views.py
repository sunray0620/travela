'''
The module that contains the audio intro views.
'''
from django.http import JsonResponse

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
