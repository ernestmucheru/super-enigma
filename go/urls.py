from django.urls import path
from . import views
from django.conf.urls.i18n import set_language



urlpatterns = [
    path('', views.home, name='base'),
    path('travels/<int:id>/', views.travel, name='travel'),
    path('create_travel/', views.createtravel, name='create_travel'),
    path('bookings/', views.bookings, name="bookings"),
    path('destinations/', views.destinations, name='destinations'),
    path('i18n/', set_language, name='set_language'),

    path('success/', views.success, name='success')
]
