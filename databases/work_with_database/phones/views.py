from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    phone_list = []
    template = 'catalog.html'
    param = request.GET.get('sort')
    if param == 'name':
        val = Phone.objects.values().order_by('name')
    elif param == 'min_price':
        val = Phone.objects.values().order_by('price')
    elif param == 'max_price':
        val = Phone.objects.values().order_by('-price')
    else:
        val = Phone.objects.values()

    for phone in val:
        phone_list.append(phone)
    context = {
               'phone_list': phone_list
                }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    val = list(Phone.objects.filter(slug=slug).values())[0]
    context = {'val': val}
    return render(request, template, context)

