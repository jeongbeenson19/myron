from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('myron.urls')),
]
