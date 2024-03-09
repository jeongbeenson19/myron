from django.urls import path
from .views import myron_views

app_name = 'myron'

urlpatterns = [
    path('myron/', myron_views.index, name='index'),
]

