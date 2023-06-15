from django.urls import path
from social_media_web import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('settings',views.settings,name='settings'),
]