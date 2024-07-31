"""
Принцип KISS в Django:

1. Простота: избегайте излишней сложности.
2. Легкость понимания: код должен быть понятен без дополнительных комментариев.
"""

# Пример: Вьюшка для отображения списка продуктов

# Сложный способ (не KISS)
from django.shortcuts import render
from .models import Product

def complex_product_list_view(request):
    products = Product.objects.all()
    product_list = []
    for product in products:
        product_list.append({
            'name': product.name,
            'price': product.price,
            'category': product.category.name
        })
    context = {
        'product_list': product_list
    }
    return render(request, 'product_list.html', context)

# Простой способ (KISS)
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Демонстрация работы KISS в Django
# product_list.html
"""
{% for product in products %}
    <p>{{ product.name }}: {{ product.price }} ({{ product.category.name }})</p>
{% endfor %}
"""
