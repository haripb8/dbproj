from django.shortcuts import render
from . models import sdb
def f(request):
    return render(request,'db1.html')
def f1(request):
    return render(request,'db2.html')
def f2(request):
    return render(request,'db3.html')
def f3(request):
    name = request.POST['name']
    age = request.POST['age']
    email = request.POST['email']
    phno = request.POST['phno']
    data = sdb(name=name, age=age, email=email, phno=phno)
    data.save()
    return render(request,'db5.html',)
def f4(request):
    name = request.POST['name']
    data1 = sdb.objects.filter(name=name)
    return render(request,'db4.html',{'data1':data1})
def f5(request):
    return render(request,'db2.html')



# Create your views here.
