from django.urls import path

from . import views


urlpatterns = [
	path('create_product/', views.create_product, name='create_product'),
	path('<int:product_id>/', views.get_sport_product, name='product'),
	path('', views.shop, name='shop'),
]