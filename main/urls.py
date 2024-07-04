from django.urls import path

from . import views

urlpatterns = [
    path('js/', views.test_js),
    path('main/', views.main, name='main'),
]