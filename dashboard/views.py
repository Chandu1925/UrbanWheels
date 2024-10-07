from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from price.models import Rental
from user.models import BikeBooking, ContactMessage, User
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect



# Create your views here.
def admin_low(request):
    return render(request,'dashboard/admin.html')

def base_table(request):
    return render(request,'dashboard/base_table.html')

def bike_book(request):
    return render(request,'dashboard/bike_book.html')

def featured(request):
    return render(request,'dashboard/featured.html')

def contact_table(request):
    return render(request,'dashboard/contact_table.html')

class create_user (APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        us = User()
        us.username = username
        us.password = password
        us.role = role
        us.save()
        return JsonResponse({"status" :  "pass"})
     


class view_user(TemplateView):
    template_name = 'dashboard/base_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = User.objects.all()
        context = {"userdata": userdata}
        return context
    

class delete_user(APIView):
    def post (self,request):
        username=request.POST.get("username")
        User.objects.filter(username=username).delete()
        return JsonResponse({"status": "pass"})
    

class update_user(APIView):
    def post (self,request):
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        User.objects.filter(username=username).update(username=username,password=password,role=role)

        return JsonResponse({"status": "pass"})
    

class create_contact (APIView):
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = ContactMessage()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return JsonResponse({"status" :  "pass"})
     


class view_contact(TemplateView):
    template_name = 'dashboard/contact_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        userdata = ContactMessage.objects.all()
        context = {"userdata": userdata}
        return context
    

class delete_contact(APIView):
    def post (self,request):
        name=request.POST["name"]
        ContactMessage.objects.filter(name=name).delete()
        return JsonResponse({"status": "pass"})


class view_book(TemplateView):
    template_name = 'dashboard/bike_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = Rental.objects.all()
        context = {"userdata": userdata}
        return context
    
class delete_book(APIView):
    def post (self,request):
        cust_name=request.POST["cust_name"]
        Rental.objects.filter(cust_name=cust_name).delete()
        return JsonResponse({"status": "pass"})
    

class view_featured(TemplateView):
    template_name = 'dashboard/featured.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = BikeBooking.objects.all()
        context = {"userdata": userdata}
        return context
    
class delete_featured(APIView):
    def post (self,request):
        phone=request.POST["phone"]
        BikeBooking.objects.filter(phone=phone).delete()
        return JsonResponse({"status": "pass"})