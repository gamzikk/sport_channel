from django.urls import path
# from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('<int:new_id>/', views.get_sport_new, name='new'),
    # path('', cache_page(60)(views.news), name='news'),
    path('', views.news, name='news'),
    path('search/', views.search, name='search'),
]