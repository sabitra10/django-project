from django.urls import path
from djangoapp import views

urlpatterns = [
   path("", views.base,name='base'),
   path("index/", views.index,name='index'),
   path("detail/<int:pk>",views.detail,name='detail'),
   path('gallery/',views.gallery,name='gallery'),
   path('contact/',views.contact,name='contact'),
] 
