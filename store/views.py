from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from store.forms import ProductForm
from store.models import Product

# Create your views here.


# @login_required
def store(request):
    products = Product.objects.all()
    # paginator = Paginator(products, 1)  # Show 25 contacts per page.

    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    context = {'my_products': products}
    return render(request, 'store/store.html', context=context)


@login_required
def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/product_info.html', context={'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('store')
        else:
            print(form.errors)
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'store/add_product.html', context=context)
