from django.urls import path
from orders.views import TrackerView, OrderView, CheckoutView


urlpatterns = [
    path('tracker/', TrackerView, name="TrackingStatus"),
    path('orders/', OrderView, name="Orders"),
    path('checkout/', CheckoutView, name="Checkout")
]
