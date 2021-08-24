from django.urls import path
from . import views

urlpatterns=[
    path('Login',views.fnLogin),
    path('Details',views.fnDetails)
]