from django.urls import path
from social_media_web import views

urlpatterns = [
    path('',views.index,name='index')
]