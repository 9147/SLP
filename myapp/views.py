from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Group
from django.contrib.auth.models import User
from django.http import JsonResponse

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
    return render(request,'myapp/account.html')

@login_required(login_url="/login/")
def UpdateGroupName(request):
    if request.method== "POST":
        group = Group.objects.get(id=request.POST['id'])
        print(group)
        group.name = request.POST['value']
        group.save()
        return JsonResponse({'status':'success'})
    return HttpResponse(404)

@login_required(login_url="/login/")
def UpdateScore(request):
    if request.method== "POST":
        group = Group.objects.get(id=request.POST['id'])
        print(group)
        if(request.POST['type'] == 'sub'):
            group.score -= int(request.POST['value'])
        else:
            group.score += int(request.POST['value'])
        group.save()
        return JsonResponse({'status':'success'})
    return HttpResponse(404)

@login_required(login_url="/login/")
def updatePassword(request,id):
    if request.method=='POST':
        user = User.objects.get(id=id)
        # print(user)
        # print(request.POST['password'])
        user.set_password(request.POST.get('password'))
        user.save()
        return HttpResponseRedirect('/account')
    return HttpResponse(404)