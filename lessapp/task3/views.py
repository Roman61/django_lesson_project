from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class MainPage(TemplateView):
    template_name = "main.html"


class ShopPage(TemplateView):
    template_name = "shop.html"


class CartPage(TemplateView):
    template_name = "cart.html"
