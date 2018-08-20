from django.urls import path
from usuario import views

urlpatterns = [
    path('', views.login, name='login'),
]
