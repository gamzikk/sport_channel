from django.urls import path

from . import views


urlpatterns = [
    path('cookie', views.test_cookie),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    # path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.user_register, name='registration'),
]
