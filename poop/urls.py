# poop/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import show_users

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path ('user/<str:phone_number>/', views.show_users, name='user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)