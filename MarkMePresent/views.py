from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import os
import csv
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,'MarkMePresent/home.html')

def data(request):
    if request.method == 'POST':
        f=open(os.path.join(settings.STATIC_ROOT, 'data/data_list.csv'), 'r')
        reader = csv.reader(f)
        for row in reader:
            if row[0]==request.POST['email'] and row[1]==request.POST['password'].upper():
                f = open(os.path.join(settings.STATIC_ROOT, 'data/attendance.csv'),'a',newline="")
                writer = csv.writer(f)
                writer.writerow([row[0],row[1],row[2]])
                f.close()
                return JsonResponse({'status':'success'})
        f.close()
        return HttpResponse(404)
    return HttpResponse(404)