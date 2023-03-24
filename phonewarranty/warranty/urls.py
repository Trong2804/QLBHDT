from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('phone/<int:pk>/', views.phone_detail, name='phone_detail'),
    path('warranty/<int:pk>/', views.warranty_detail, name='warranty_detail'),
]
