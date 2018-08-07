from django.urls import path
from suite import views

urlpatterns = [
    path('', views.index, name='index'),
]
