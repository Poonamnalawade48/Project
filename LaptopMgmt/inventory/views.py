# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
# pagination
def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 25)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'list.html', {'products': products})