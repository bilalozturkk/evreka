from django.urls import path

from . import views

app_name = 'question_1'
urlpatterns = [
    path('', views.get_last_points_per_vehicle, name='index'),
]