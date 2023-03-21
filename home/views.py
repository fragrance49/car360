from django.shortcuts import render
from django.http import HttpResponse

from home.models import Blog
from home.serializers import BlogSerializer
# from rest_framework.viewsets import ModelViewSet

from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
from rest_framework import status
 
# from rest_framework.decorators import api_view
from requests.auth import HTTPBasicAuth
import requests

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# Create your views here.
def home(request):    
    context ={}
    context["dataset"] = Blog.objects.all() 
    return render(request, 'home/index.html', context)
    

    # return render(request, 'home/index.html', {})

def services(request):
    return render(request, 'home/services.html', {})


def test(request):    

    return render(request, "home/vinnum.html", {})

# def validate(request):
#    if request.method == 'POST':
#       vin_number= request.POST["vin_number"]
#       print(vin_number)
    


def Apicall(request):
    # return render(request, "home/test.html", {'users': users})
    if request.method == 'POST':
        vin_number= request.POST["vin_number"]
        print(vin_number)
        r = requests.post('https://us-central1-glo3d-c338b.cloudfunctions.net/api', data ={'vin_number':vin_number}, auth = HTTPBasicAuth('info@activedevtech.com', '2rdFUSR01j4'))  
        # print(r.json())
        data = r.json()
        # print(data)
        # t_data = JSONParser().parse(request)
        t_serializer = BlogSerializer(data=data)
        if t_serializer.is_valid():
            t_serializer.save()
            return JsonResponse(t_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(t_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # return render(request, "home/test.html", {'data':data})


