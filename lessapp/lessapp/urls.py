"""
URL configuration for lessapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

#from task5.views import MainPage, shop_page, CartPage, MenuWidget
from task5.views import sign_up_by_django, sign_up_by_html

# from app.views import func_template, ClassTemplate

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cart/', CartPage.as_view()),
#     path('main/', MainPage.as_view()),
#     path('shop/', shop_page),
#     path('menu/', MenuWidget.as_view())
# ]

urlpatterns = [
    path('', sign_up_by_django, name='sign_up_by_django'),
    path('django_sign_up/', sign_up_by_html, name='sign_up_by_html'),
]
