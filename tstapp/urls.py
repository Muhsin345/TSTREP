from django.urls import path
from . import views

urlpatterns=[
    path('Login1/',views.fnLogin),
    path('Details/',views.fnDetails),
    path('Userhome/',views.fnUser),
    path('fbhome/',views.fnFB),
    path('prdcts/',views.fnprdcts),
    path('bootstrap/',views.fnnav),
    path('gridnav/',views.fngrid),
    path('facebook/',views.facebook),
    path('sample/',views.navsmpl)
]