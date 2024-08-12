from django.urls import path
from . import views

urlpatterns = [
    path('bgevent/', views.bgevent, name='bgevent'),
]
