from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Product, Order, Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Главная страница с каталогом товаров
#@login_required  # Применяем декоратор для проверки авторизации
def catalog(request):
    products = Product.objects.all()[:6]  # Отображаем только 6 товаров
    return render(request, 'flowers/catalog.html', {'products': products})

@login_required(login_url='/accounts/login/')  # Перенаправляем на страницу логина, если пользователь не авторизован
def place_order(request):
    if request.method == 'POST':
        user = request.user  # Получаем текущего аутентифицированного пользователя
        products = request.POST.get('products')  # Получаем товары из формы
        product_ids = request.POST.getlist('products')  # Получаем список ID товаров
        print("User:", user)
        print("Product IDs:", product_ids)
        if not product_ids:
            all_products = Product.objects.all()  # Получаем все продукты
            return render(request, 'place_order.html',
                          {'products': Product.objects.all(), 'error': 'Выберите хотя бы один товар.'})
        selected_products = request.POST.getlist('products')
        order = Order(user=request.user)
        order.save()
        order.products.set(selected_products)
        new_order = Order.objects.create(user=user,            # Передача пользователя
            status='pending'      # Установка статуса заказа
            )
        selected_products = Product.objects.filter(id__in=product_ids)
        new_order.products.set(selected_products)
        return redirect('order_success', order_id=new_order.id)
    else:
        all_products = Product.objects.all()
        return render(request, 'flowers/place_order.html', {'products': all_products})

# Оставить отзыв
def leave_review(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        review_text = request.POST['review']
        rating = request.POST['rating']
        review = Review(user=request.user, product=product, review=review_text, rating=rating)
        review.save()
        return redirect('product_detail', product_id=product.id)
    return render(request, 'flowers/leave_review.html', {'product_id': product_id})

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'flowers/order_success.html', {'order': order})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # После успешной регистрации перенаправляем на логин
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required  # Ограничиваем доступ только авторизованным пользователям
def profile(request):
    return render(request, 'flowers/profile.html')  # Убедитесь, что у вас есть соответствующий шаблон


@login_required
def order_detail(request, order_id):
    # Получаем заказ по id или возвращаем 404, если не найдено
    order = get_object_or_404(Order, id=order_id, user=request.user)  # Заказ принадлежит текущему пользователю

    context = {
        'order': order,
        'products': order.products.all(),  # Получаем связанные товары
    }
    return render(request, 'flowers/order_detail.html', context)