from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Group
from django.contrib.auth.models import User
from django.http import JsonResponse
import re
import csv

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    a=Group.objects.all()
    # print(a)
    type = "none"
    groupvalue = None
    for group in a:
        if request.user == group.leader:
            type="leader"
            groupvalue=group
            break
        elif request.user in group.members.all():
            type="member"
            groupvalue=group
            break
    return render(request,'myapp/home.html',context={'groups':a,'type':type,'group':groupvalue})

@login_required(login_url="/login/")
def about(request):
    return render(request,'myapp/about.html')

@login_required(login_url="/login/")
def account(request):
    user=User.objects.get(id=request.user.id)
    group=Group.objects.filter(members=user)
    type="member"
    if(len(group)==0):
        type="leader"
        group=Group.objects.filter(leader=user)
    # print(group)
    if len(group)==0:
        type="none"
        group=None
    else:
        group=group[0]
    return render(request,'myapp/account.html',context={'group':group,'type':type})

@login_required(login_url="/login/")
def UpdateGroupName(request):
    if request.method== "POST":
        group = Group.objects.get(id=request.POST['id'])
        # print(group)
        group.name = request.POST['value']
        group.save()
        return JsonResponse({'status':'success'})
    return HttpResponse(404)

@login_required(login_url="/login/")
def UpdateScore(request):
    if request.method== "POST":
        group = Group.objects.get(id=request.POST['id'])
        # print(group)
        if(request.POST['type'] == 'sub'):
            group.score -= int(request.POST['value'])
        else:
            group.score += int(request.POST['value'])
        group.save()
        return JsonResponse({'status':'success'})
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def updatePassword(request,id):
    if request.method=='POST':
        user = User.objects.get(id=id)
        # print(user)
        # print(request.POST['password'])
        user.set_password(request.POST.get('password'))
        user.save()
        return HttpResponseRedirect('/account')
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def createusers(request):
    # print(request.POST)
    # user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'))
    # user.save()
    if request.user.is_superuser:
        return render(request,'myapp/createusers.html')
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def updateUsers(request):
    if request.method=='POST':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # print(request.POST)
        dic=request.POST.dict()
        # print(dic)
        val=0
        li=[]
        a=[]
        for key in dic:
            if val==4:
                val=0
                li.append(a)
                a=[key[:-11]]
            elif val==0:
                a=[key[:-11]]
            a.append(dic[key])
            if val==2:
                if not re.fullmatch(regex, dic[key]):
                    # print("Invalid Email",key,dic[key])
                    return HttpResponse(status=404)
            # print(key,dic[key])
            val+=1
            # print(val)
        li.append(a)
        print(li)
        for a in li:
            if User.objects.filter(username=a[0]).exists():
                user=User.objects.get(username=a[0])
                user.first_name=a[1]
                user.last_name=a[2]
                user.email=a[3]
                user.set_password(a[4])
                user.save()
            else:
                user = User.objects.create_user(username=a[0],password=a[4],email=a[3],first_name=a[1],last_name=a[2])
                user.save()
                # print("Username already exists")
        # user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'))
        # user.save()
        return HttpResponseRedirect('/')
    return HttpResponse(status=404)

@login_required(login_url="/login/")
def resetGame(request):
    if request.method=='POST':
        groups=Group.objects.all()
        for group in groups:
            group.score=1000
            group.save()
        with open('movies.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        # Displaying the data read from the CSV file
        data= data[1:]
        for row in data:
            print(row)
        return JsonResponse({'status':'success'})
    return HttpResponse(status=404)
