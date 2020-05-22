from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('fetch',views.fetch_destination),
    path('checkout',views.checkout)
]
