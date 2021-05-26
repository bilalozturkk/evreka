from django.urls import path

from . import views

app_name = 'question_2'
urlpatterns = [
    path('', views.get_collection_frequency_list, name='index'),
]