from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Product

# Create your views here.
def home_view(request):
    return render(request, 'invApp/home.html')

def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {
        'form': form
    }
    return redirect(request, 'invApp/product_form.html', context)

def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'invApp/product_list.html', context)

def product_update_view(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {
        'form': form,
        'product': product
    }
    return redirect(request, 'invApp/product_form.html', context)

def product_delete_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {
        'product': product
    }
    return render(request, 'invApp/product_confirm_delete.html', context)
