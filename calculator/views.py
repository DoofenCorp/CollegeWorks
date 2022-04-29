from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request, "index.html", {"Add_Result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "index.html", {"Add_Result": res})
    
def sub(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a - b

        return render(request, "index.html", {"Sub_Result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "index.html", {"Sub_Result": res})

def multiply(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b

        return render(request, "index.html", {"Mul_Result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "index.html", {"Mul_Result": res})

def divide(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a / b

        return render(request, "index.html", {"Div_Result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "index.html", {"Div_Result": res})