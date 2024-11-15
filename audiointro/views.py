'''
The module that contains the audio intro views.
'''
import base64
import json
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

from audiointro.libs.audio_intro_retriever import AudioIntroRetriever
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient
from shared.gcloud_client.texttospeech_client import TextToSpeechClient
from shared.gcloud_client.gcs_client import GcsClient

def audio_intro(request):
    '''Post method to retrieve audio intro'''
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        return render(request, 'audiointro/get_audio_intro.html')

    # Handle the POST request here
    data = json.loads(request.body)
    query = data.get('query', '')
    generativelanguage_client = GenerativeLanguageClient()
    texttospeech_client = TextToSpeechClient()
    audio_intro_retriever = AudioIntroRetriever(generativelanguage_client, texttospeech_client)
    resp = audio_intro_retriever.get_audio_intro(query)
    return JsonResponse(resp)


def download_audio(request) -> str:
    '''GET method to retrieve audio file'''
    audio_bucket_name = 'travela-bucket'
    audio_folder_name = 'audios'

    if request.GET.get('audio_tour_id'):
        audio_tour_id = request.GET.get('audio_tour_id')
    else:
        resp = JsonResponse({
            'error': 'Do not find audio tour ID'
        })
        resp.status_code = 400
        return resp

    audio_blob_name = f'{audio_folder_name}/{audio_tour_id}.mp3'

    gcs_client = GcsClient()
    byte_array = gcs_client.download_blob(
        bucket_name=audio_bucket_name, source_blob_name=audio_blob_name)
    file_content_string = base64.b64encode(byte_array).decode('ascii')
    resp = {
        'audioContent': file_content_string,
    }
    return JsonResponse(resp)
