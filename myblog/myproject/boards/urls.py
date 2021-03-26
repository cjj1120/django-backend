from django.urls import path
from . import views
#. is the current directory 


urlpatterns = [
    path('', views.home, name='blog-home'),

]