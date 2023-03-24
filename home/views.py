from django.shortcuts import render
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
    context['datafields'] = Blog.objects.values_list('fields', flat=True)
    global make_arr
    global model_arr
    make_arr = []
    model_arr = []
    global messages
    messages = []

    # if len(context["datafields"] ) != 0:
    #     for x in context["datafields"] :
    #         # print(x)
    #         if x[0].key == 'make':
    #             make_arr.append(x)
    #         elif x[0].key == 'model':
    #             model_arr.append(x)
    #         else:
    #             pass
    # print(make_arr)
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


