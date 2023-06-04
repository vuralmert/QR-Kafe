from django.shortcuts import render, HttpResponse
from orders.models import Orders, OrderUpdate
from django.contrib import messages
from django.contrib.auth import authenticate
import json

# Create your views here.


def TrackerView(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:
            try:
                order = Orders.objects.filter(order_id=orderId, email=email)
                if len(order) > 0:
                    update = OrderUpdate.objects.filter(order_id=orderId)
                    updates = []
                    for item in update:
                        updates.append({'text': item.update_desc, 'time': item.timestamp})
                        response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                    return HttpResponse(response)
                else:
                    return HttpResponse('{"status":"noitem"}')
            except Exception as e:
                return HttpResponse('{"status":"error"}')
        else:
            return HttpResponse('{"status":"Invalid"}')
    return render(request, 'tracker.html')


def OrderView(request):
    if request.user.is_authenticated:
        current_user = request.user
        orderHistory = Orders.objects.filter(userId=current_user.id)
        if len(orderHistory) == 0:
            messages.info(request, "Henüz bir sipariş vermediniz.")
            return render(request, 'orderView.html')
        return render(request, 'orderView.html', {'orderHistory': orderHistory})
    return render(request, 'orderView.html')


def CheckoutView(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        user_id = request.POST.get('user_id', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        table_no = request.POST.get('table_no', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, userId=user_id, name=name, email=email, table_no=table_no, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Siparişiniz hazırlanıyor..")
        update.save()
        thank = True
        id = order.order_id
        if 'cashOnDelivery' in request.POST:
            return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')
