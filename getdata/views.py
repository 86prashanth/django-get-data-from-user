from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def result(request):
    result=request.GET['result']
    num1=int(request.GET['first'])
    num2=int(request.GET['second'])
    sum=num1+num2
    return render(request,'app/result.html',{'sum':sum,'result':result})