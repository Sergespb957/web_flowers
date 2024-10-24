from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [

    path('catalog/', views.catalog, name='catalog'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
    path('leave_review/', views.order_success, name='leave_review'),
    path('profile/', views.profile, name='profile'),  # Новый маршрут для профиля
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('accounts/', include('django.contrib.auth.urls')),  # Включаем стандартные маршруты аутентификации Django
    path('signup/', views.signup, name='signup'),  # Регистрация
    #path('flowers/', include('flowers.urls')),  # Маршруты приложения "flowers"
]
