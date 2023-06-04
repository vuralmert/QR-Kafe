# Create your views here.

from django.shortcuts import render
from pages.models import Contact, Product
from math import ceil


def HomeView(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    mv_dict = {'allProds': allProds}
    return render(request, 'index.html', mv_dict)


def ProjectView(request):
    return render(request, 'project.html')


def AboutView(request):
    return render(request, 'about.html')


def ContactView(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'contact.html', {'thank': thank})
    return render(request, 'contact.html', {'thank': thank})


def SearchView(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    mv_dict = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 3:
        mv_dict = {'msg': "Aramanıza uygun sonuç bulunamadı. Lütfen tekrar deneyin."}
    return render(request, 'search.html', mv_dict)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.desc or query in item.product_name or query in item.category or query in item.desc.upper() or query in item.product_name.upper() or query in item.category.upper():
        return True
    else:
        return False

def ProductView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'prodView.html', {'product': product[0]})