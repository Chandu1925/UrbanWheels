from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from price.models import Rental

def pricing (request):
    return render(request,'price/pricing.html')

def bike_list(request):
    return render(request,'price/bike_list.html')

def payment_page(request):
    return render(request, 'price/payment.html')

def process_payment(request):
    return render(request, 'price/process_payment.html')
            
class submit_rental (APIView):
    def post(self,request):
        cust_name = request.POST['cust_name']
        email = request.POST['email']
        bike_name = request.POST['bike_name']
        rental_type = request.POST['rental_type']
        price = request.POST['price']
        rental = Rental()
        rental.cust_name = cust_name
        rental.email = email
        rental.bike_name = bike_name
        rental.rental_type = rental_type
        rental.price = price
        rental.save()
        return JsonResponse({"status" :  "pass"})