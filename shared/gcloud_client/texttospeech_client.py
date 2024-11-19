'''
This module interacts with TextToSpeech on Google Cloud.
'''
from google.cloud import texttospeech

SUPPORTED_LANGUAGES = {
    'en-US': {'language_code': 'en-US', 'voice_name': 'en-US-Journey-F'},
    'cn-ZH': {'language_code': 'cmn-CN', 'voice_name': 'cmn-CN-Wavenet-A'}
}

class TextToSpeechHttpClient:
    '''TextToSpeech Client.'''
    def generate_speech(self, text, language) -> str:
        '''Get audio speech content.'''
        if language not in SUPPORTED_LANGUAGES:
            return None
        language_config = SUPPORTED_LANGUAGES[language]

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_config['language_code'],
            name=language_config['voice_name']
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        return response.audio_content
