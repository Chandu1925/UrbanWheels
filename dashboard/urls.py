from django.urls import path
from . import views

urlpatterns = [

    path("",views.admin_low,name='admin_low'),
    path("base_table",views.base_table,name='base_table'),
    path("bike_book",views.bike_book,name='bike_book '),
    path("featured",views.featured,name='featured '),
    path("view_featured",views.view_featured.as_view(),name="view_featured"),
    path("delete_featured",views.delete_featured.as_view(),name="delete_featured"),
    path("contact_table",views.contact_table,name='contact_table'),
    path("create_user",views.create_user.as_view(),name="create_user"),
    path("view_user",views.view_user.as_view(),name="view_user"),
    path("update_user",views.update_user.as_view(),name="update_user"),
    path("delete_user",views.delete_user.as_view(),name="delete_user"),
    path("view_book",views.view_book.as_view(),name="view_book"),
    path("delete_book",views.delete_book.as_view(),name="delete_book"),
    path("create_contact",views.create_contact.as_view(),name="create_contact"),
    path("view_contact",views.view_contact.as_view(),name="view_contact"),
    path("delete_contact",views.delete_contact.as_view(),name="delete_contact"),
]


