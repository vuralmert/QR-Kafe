from django.urls import path
from pages.views import ProjectView, HomeView, AboutView, ContactView, ProductView, SearchView


urlpatterns = [
    path('', ProjectView, name="Project"),
    path('home/', HomeView, name="Home"),
    path('about/', AboutView, name="AboutUs"),
    path('contact/', ContactView, name="ContactUs"),
    path('productView/<int:myid>', ProductView, name="Product"),
    path('search/', SearchView, name="Search"),
]
