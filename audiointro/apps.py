'''
The module that contains the app configs.
'''
from django.apps import AppConfig


class AudiointroConfig(AppConfig):
    '''The class that contains the app configs for audiointro.'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'audiointro'
