from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import CreateProductForm


def shop(request):
	products = Product.objects.order_by('-created_at')
	return render(request, 'shop/shoplist.html', {'products': products})


def get_sport_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'shop/product.html', {'product': product})


def create_product(request):
	if request.method == 'POST':
		product_form = CreateProductForm(request.POST, request.FILES)
		if product_form.is_valid():
			post = product_form.save(commit=False)
			post.user = request.user
			post.save()
			#product_form.save()
			return HttpResponse('Объявление успешно размешено на сайте')
		else:
			return HttpResponse('неправильно')
	else:
		product_form = CreateProductForm()
	return render(request, 'shop/create_product.html', {'product_form': product_form})