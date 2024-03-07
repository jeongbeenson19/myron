from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from myron.views import myron_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth.html'), name='login'),
    path('admin/', admin.site.urls),
    path('myron/', include('myron.urls')),
    path('myron/', myron_views.index, name='index')
]
