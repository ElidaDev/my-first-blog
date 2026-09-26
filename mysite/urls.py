"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django Girls Tutorial - "Django URLs" chapter:
    # send everything else off to blog/urls.py
    path('', include('blog.urls')),
]
