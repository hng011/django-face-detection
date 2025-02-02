"""
URL configuration for django_face_detection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index
from detections.views import (
    video_feed, 
    start_cam,
    stop_cam
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('video_feed', video_feed, name="video_feed"),
    path('start_cam', start_cam, name='start_cam'),
    path('stop_cam', stop_cam, name='stop_cam')
]
