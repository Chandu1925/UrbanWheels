from django.urls import path
from . import views

urlpatterns = [
    path("pricing/",views.pricing,name='pricing'),
    path("bike_list/",views.bike_list,name='bike_list'),
    path("submit_rental/", views.submit_rental.as_view(), name='submit_rental'),
    path('payment/', views.payment_page, name='payment_page'),
     path('process_payment/', views.process_payment, name='process_payment'),
]
    