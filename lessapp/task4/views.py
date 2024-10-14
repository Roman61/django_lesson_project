from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "main.html"


class CartPage(TemplateView):
    template_name = "cart.html"


class MenuWidget(TemplateView):
    template_name = "menu.html"


def shop_page(request):
    print("shop_page called")
    context = {
        'games': ["Atomic Heart", "Cyberpunk 2077"]
    }
    return render(request, 'fourth_task/shop.html', context)
