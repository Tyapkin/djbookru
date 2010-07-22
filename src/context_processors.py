from django.conf import settings 
from django import get_version

def custom(request):
    return {
        'debug': settings.DEBUG,
        'google_analytics': settings.GOOGLE_ANALYTICS,
        'django_version': get_version()
    }