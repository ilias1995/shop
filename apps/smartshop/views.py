from django.shortcuts import get_object_or_404, render

from models import Product, NameProduct



def index(request):
	product = Product.objects.all()
	nameproduct = NameProduct.objects.all().order_by('-name')
	return render(request, 'smartshop/index.html', {'nameproduct':nameproduct,'product':product})


def detail(request, nameproduct_id):
    namepro = NameProduct.objects.all().order_by('-name')
    nameproduct = get_object_or_404(NameProduct, pk=nameproduct_id)
    return render(request, 'smartshop/detail.html', {'nameproduct': nameproduct, 'namepro':namepro})

def info(request, id):
	product = Product.objects.get(pk=id)
	return render(request, 'smartshop/info.html', {'product': product})