from django.shortcuts import render,redirect
from django.http import HttpResponse

from home.models import Blog
from home.serializers import BlogSerializer

from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view
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


@api_view(['GET', 'PUT', 'DELETE'])
def details(request, pk):
    d_data = Blog.objects.get(short_id=pk) 
    if request.method == 'GET': 
        blog_serializer = BlogSerializer(d_data) 
        # return JsonResponse(blog_serializer.data)
        return render(request, 'home/details.html', {'data' : blog_serializer.data})

def services(request):
    return render(request, 'home/services.html', {})


def test(request):    
    return render(request, "home/vinnum.html", {})


def Apicall_test(request):
    # return render(request, "home/test.html", {'users': users})
    if request.method == 'POST':
        vin_number= request.POST["vin_number"]
        print(vin_number)  
        return render(request, "home/vinnum.html", {})

def Apicall(request):
    # return render(request, "home/test.html", {'users': users})
    if request.method == 'POST':
        vin_number= request.POST["vin_number"]
        # print(vin_number)
        r = requests.post('https://us-central1-glo3d-c338b.cloudfunctions.net/api', data ={'vin_number':vin_number}, auth = HTTPBasicAuth('info@activedevtech.com', '2rdFUSR01j4'))  
        # print(r.json())
        data = r.json()
        # print(data)
        # t_data = JSONParser().parse(request)
        t_serializer = BlogSerializer(data=data)
        if t_serializer.is_valid():
            t_serializer.save()
            # return JsonResponse(t_serializer.data, status=status.HTTP_201_CREATED) 
            # return JsonResponse()
            return redirect('/')
        return JsonResponse(t_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # return render(request, "home/test.html", {'data':data})


def perutest(request):
    
    return render(request, "home/perutest.html", {})
    pass



