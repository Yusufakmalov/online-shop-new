from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                    slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                     'main/index.html',
                    {'category': category,
                     'categories': categories,
                     'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                    'shop/product/detail.html',
                    {'product': product,
                    'cart_product_form': cart_product_form})

def accessories(request):   
    accessories = Product.objects.filter(category__name="Accessories")
    return render(request, 'main/store.html', {'accessories': accessories})               



def homepage(request):
    return render(request, 'index.html',
                {'nav_items': ['Home', 'Hot Deals',
                'Categories', 'Laptops', 'Smartphones',
                'Cameras', 'Accessories']})

def hot_deals(request):
    hot_deals = Product.objects.filter(is_hot_deal=True)
    return render(request, 'shop/hot_deals.html', {'hot_deals': hot_deals})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

def laptops(request):
    laptops = Product.objects.filter(category="Laptops")
    return render(request, 'shop/laptops.html', {'laptops': laptops})

def smartphones(request):
    smartphones = Product.objects.filter(category="Smartphones")
    return render(request, 'shop/smartphones.html', {'smartphones': smartphones})

def cameras(request):       
    cameras = Product.objects.filter(category="Cameras")
    return render(request, 'shop/cameras.html', {'cameras': cameras})   





