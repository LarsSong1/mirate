from django.contrib import admin
from django.urls import path
from .views import *
from mirate import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView, name="home-view")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)