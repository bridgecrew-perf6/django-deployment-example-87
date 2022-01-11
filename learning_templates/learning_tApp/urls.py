from django.urls import path
from learning_tApp import views

# TEMPLATES TAGGING:

app_name = 'learning_tApp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]