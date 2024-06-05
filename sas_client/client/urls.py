from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sentiment_analysis, name='get_sentiment_analysis'),
    path('create/', views.create_sentiment_analysis, name='create_sentiment_analysis'),
]