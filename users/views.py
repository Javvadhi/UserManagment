from django.shortcuts import render,redirect
from users.models import User
from users.forms import UserForm

def post(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass 
    else:
        form = UserForm

    return render(request,'temp.html',{'form':form})

def get(request,uid):
    users = User.objects.get(uid=uid)
    return render(request.'temp.html',{'users':users})

def update(request,uid):
    users = User.objects.get(uid=uid)
    form =UserForm(request.POST, instance = users) 
    if form.is_valid():
        form.save()
    return render(request.'temp.html',{'form':form})

def delete(request,uid):
    users = User.objects.get(uid=uid)
    users.delete()
    return redirect("html")



