from django.urls import path, include
from .views import myron_views

urlpatterns = [
    path('', myron_views.index, name='index'),
]