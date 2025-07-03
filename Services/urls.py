from django.urls import path
from . import views

app_name = 'Services'

urlpatterns = [
    path('', views.home , name='home'),
    path('service', views.service , name='service'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('book', views.book , name='book'),
    path('register', views.register , name='register'),
    path('login', views.login , name='login'),
    path('logout', views.logout , name='logout'),
]

