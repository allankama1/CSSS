
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('innerpage/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='register'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointmentdetails/', views.appointmentdetails, name='appointment details'),
    path('products/', views.details, name='products'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
