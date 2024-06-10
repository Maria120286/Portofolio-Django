from django.urls import path
from . import views

app_name = 'portofolio'
urlpatterns = [
    path('', views.index, name='home')
]
