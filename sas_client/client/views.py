from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import requests


def get_sentiment_analysis(request):
    response = requests.get(f'{settings.BACKEND}/sentiment-analysis/')
    sentiment_data = response.json().get('results', []) if response.status_code == 200 else []
    return render(request, 'index.html', {'sentiment_data': sentiment_data})


def create_sentiment_analysis(request):
    if request.method == 'POST':
        text = request.POST['text']
        response = requests.post(f'{settings.BACKEND}/sentiment-analysis/create/', json={'text': text})
        if response.status_code == 201:
            return HttpResponseRedirect('/')
        else:
            error_message = response.json().get('error', 'Error during sentiment analysis.')
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return HttpResponseRedirect('/')
