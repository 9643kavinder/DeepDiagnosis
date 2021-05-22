from json.encoder import JSONEncoder
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserInfo
from django.views.decorators.csrf import csrf_exempt
import re
import random
# from django.db.models import Q
# Create your views here.
def home(request):
    return JsonResponse({"name": "Kavinder Panwar", "age": "22"})

@csrf_exempt
def signup(request):
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']
    gender = request.POST['gender']
    name = request.POST['name']
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


def generate_session_token(length=10):
    return "".join(random.SystemRandom().choice([chr(i) for i in range(97,123)]) for _ in range(10))

@csrf_exempt
def login(request):
    email = request.POST['email']
    password = request.POST['password']
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

@csrf_exempt
def logout(request, id):
    try:
        user = UserInfo.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserInfo.DoesNotExist:
        return JsonResponse(dict(status=0, message="Invalid User Id"))
    return JsonResponse(dict(status=1, message="Successfully Logged Out"))


    