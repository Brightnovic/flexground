
from django.urls import path
from . import views


app_name = 'take_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('getnames/', views.get_names, name='get_names'),
]
