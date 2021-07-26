from django.shortcuts import render
from .models import *
# Create your views here.

def result_view(request):
    no_of_users = Individual_result.objects.count()
    total_res = Total_result.objects.first()
    obj = Individual_result.objects.all()
    context={
        'no_of_users' : no_of_users,
        'res' : total_res,
        'obj' : obj
    }
    return render(request,"result/result.html",context)