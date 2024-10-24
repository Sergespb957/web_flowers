"""
URL configuration for mysite project.

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
from django.urls import path, include
from django.shortcuts import redirect
from flowers import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ панель
    path('', lambda request: redirect('catalog'), name='home'),  # Перенаправление на каталог
    path('accounts/', include('django.contrib.auth.urls')),  # Маршруты для login, logout и т.д.
    path('signup/', views.signup, name='signup'),  # Маршрут для регистрации
    path('flowers/', include('flowers.urls')),  # Подключаем URL-ы из приложения flowers
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)