from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    name = "Shoaib Rahman Shajid"
    demo_list = ["Lemborghini Essenza SV12","Buggati Bolide W16.4"]
    dict = {"name":name,"list":demo_list}
    return render(request, 'portfolio.html')