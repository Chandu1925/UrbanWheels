from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from user.models import BikeBooking, ContactMessage, User
from django.shortcuts import render, redirect


# Create your views here.
def index (request):
    return render(request,'user/index.html')

def login (request):
    return render(request,'user/login.html')

def register (request):
     return render(request,'user/register.html')

def contact (request):
    return render(request,'user/contact.html')

def book_bike (request):
    return render(request,'user/book_bike.html')

class login_check(APIView):
        def post(self,request):
            username = request.POST["username"]
            password = request.POST["password"]
            print("username: ",username)
            print("password: ",password)
            us = User.objects.filter(username=username,password=password ).values()
            print("*********:",us)
            if len(us) > 0:
                return JsonResponse({"status":"pass", "user": us[0]["username"], "role": us[0]["role"]})
            else:
                return JsonResponse({"status":"fail"})
            


# views.py

class bike_book(APIView):
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        bike_model = request.POST['bike_model']
        booking_date = request.POST['booking_date']
        rental_days = request.POST['rental_days']
        price = request.POST['price']
        bike = BikeBooking()
        bike.name = name
        bike.email = email
        bike.phone=phone
        bike.bike_model=bike_model
        bike.booking_date = booking_date
        bike.rental_days=rental_days
        bike.price=price
        bike.save()
        return JsonResponse({"status" :  "pass"})





# views.py

class message(APIView):
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        msg = ContactMessage()
        msg.name = name
        msg.email = email
        msg.subject=subject
        msg.message=message
        msg.save()
        return JsonResponse({"status" :  "pass"})


