from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('Apicall',views.Apicall,name="Apicall"),
    path('Vehicles', views.home, name='home'),
    path('service-department/', views.services, name='services'),
]
