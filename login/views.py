from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from myapp.views import home


# Create your views here.
def loginMe(request):
    return render(request,'login/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("success")
            return JsonResponse({'data':'success'})
        else:
            return HttpResponse(status=401)
    return HttpResponse(status=404)

def logoutPage(request):
    logout(request)
    return home(request)

