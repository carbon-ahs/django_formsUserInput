from django.urls import path
from . import views
urlpatterns = [
    path('', views.contact, name='contact'),
    path('in', views.snippet, name='snippet'),
    path('out', views.out, name='out'),
    
]