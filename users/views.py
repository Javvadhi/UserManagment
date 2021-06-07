from django.shortcuts import render
from users.models import User
from django.http import JsonResponse

def post(request):
    users = User.objects.save()
    return JsonResponse({'users':users})

def get(request,uid):
    users = User.objects.get(uid=uid)
    return JsonResponse({'users':users})

def update(request,uid):
    users = User.objects.get(uid=uid)
    users = users.objects.save()
    return JsonResponse({'users':users})

def delete(request,uid):
    users = User.objects.get(uid=uid)
    users.delete()



