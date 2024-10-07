from django.urls import path
from . import views



urlpatterns = [

    path("",views.index,name='index'),
    path("login/",views.login,name="login"),
    path("login_check",views.login_check.as_view(),name="login_check"),
    path("register/",views.register,name="register"),
    path("contact/",views.contact,name="contact"),
    path('book_bike/', views.book_bike, name='book_bike'),
    path("message/",views.message.as_view(),name="message"),
    path("bike_book/",views.bike_book.as_view(),name="bike_book"),
    
]