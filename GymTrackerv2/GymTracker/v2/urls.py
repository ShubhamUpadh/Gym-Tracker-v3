from django.urls import path, include
from v2 import views

urlpatterns = [
    path("",views.home_view,name='home_view')
]
