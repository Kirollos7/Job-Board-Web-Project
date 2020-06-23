from django.urls import path 
from . import views
urlpatterns = [
    
path('a/',views.about,name='about')
]