from json.encoder import JSONEncoder
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
import re
import random
# from django.db.models import Q
# Create your views here.
def home(request):
    return JsonResponse({"name": "Kavinder Panwar", "age": "22"})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            phone = request.POST['phone']
            gender = request.POST['gender']
            name = request.POST['name']
        except:
            return JsonResponse(dict(status=0, message="Invalid Parameters"))
        try:
            user = UserInfo.objects.get(email=email)
            return JsonResponse(dict(status=0, message="Email or Phone Already Exists"))
        except ObjectDoesNotExist:
            user = UserInfo.objects.create(email=email, password=password, 
                    phone=phone, gender=gender, name=name)
            user.save()
            return JsonResponse(dict(status=1, message="User Succesfully Registered"))
        # except MultipleObjectsReturned:
        #     return JsonResponse(dict(status=0, message="Email or Phone Already Exists."))
    else:
        return JsonResponse(dict(status=0, message="Invalid Request Method"))

def generate_session_token(length=10):
    return "".join(random.SystemRandom().choice([chr(i) for i in range(97,123)]) for _ in range(10))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
        except:
            return JsonResponse(dict(status=0, message="Invalid Parameters"))
        try:
            user = UserInfo.objects.get(email=email)
            if user.password == password:
                if user.session_token != "0":
                    user.session_token = "0"
                    user.save()
                    return JsonResponse(dict(status=0, message="User Already Loggedin"))
                token = generate_session_token()
                user.session_token = token
                user_id = user.id
                user.save()
                return JsonResponse(dict(status=1, token=token, id=user_id))
            else:
                return JsonResponse(dict(status=0, message="Wrong Credentials, Try Again"))
        except:
            return JsonResponse(status=0, message="User Does Not Exists")

    else:
        return JsonResponse(dict(status=0, message="Invalid Request Method"))

@csrf_exempt
def logout(request, id):
    try:
        user = UserInfo.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserInfo.DoesNotExist:
        return JsonResponse(dict(status=0, message="Invalid User Id"))
    return JsonResponse(dict(status=1, message="Successfully Logged Out"))


@csrf_exempt
def get_profile(request, id):
    if request.method == 'GET':
        try:
            snippets = UserInfo.objects.get(pk=id)
            serializer = UserInfoSerializer(snippets)
            return JsonResponse(dict(status=1, data=serializer.data))

        except UserInfo.DoesNotExist:
            return JsonResponse(dict(status=0, message="Invalid User Id"))

    else:
        return JsonResponse(dict(status=0, message="Invalid Request Method"))


@csrf_exempt
def update_profile(request, id):
    if request.method == 'POST':
        try:
            user = UserInfo.objects.get(pk=id)
            try:
                phone = request.POST['phone']
                gender = request.POST['gender']
                name = request.POST['name']
            except:
                return JsonResponse(dict(status=0, message="Invalid Parameters"))
            user.phone = phone
            user.gender = gender
            user.name = name
            user.save()
            serializer = UserInfoSerializer(user)
            return JsonResponse(dict(status=1, data=serializer.data))

        except UserInfo.DoesNotExist:
            return JsonResponse(dict(status=0, message="Invalid User Id"))

    else:
        return JsonResponse(dict(status=0, message="Invalid Request Method"))

@csrf_exempt
def find_labs(request):
    if request.method == 'GET':
        try:
            test = request.GET['test'].lower()
            city = request.GET['city'].lower()
            state = request.GET['state'].lower()
        except:
            return JsonResponse(dict(status=0, message="Invalid Parameters"))
        
        objs = CompanyTest.objects.filter(test=test, city=city, state=state)
        data = []
        for obj in objs:
            context = dict()
            context['company_name'] = obj.company.company_name.title()
            context['area'] = obj.area
            context['image'] = "http://127.0.0.1:8000/images/"+str(obj.company.image)
            context['price'] = obj.price
            data.append(context)

        return JsonResponse(dict(status=1, test=test.title(), city=city.title(), state=state.title(), data=data))
    else:
        return JsonResponse(dict(status=0, message="Invalid Request Method"))