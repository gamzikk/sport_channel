from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main/main.html')


def test_js(request):
    return render(request, 'main/index.html')