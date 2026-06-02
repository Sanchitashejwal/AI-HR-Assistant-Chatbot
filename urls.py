from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_api, name='chat_api'),
    path('submit-resignation/', views.submit_resignation, name='submit_resignation'),
]
