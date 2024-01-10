from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from . models import About

def demo(request):
    name = "Shoaib Rahman Shajid"
    demo_list = ["Lemborghini Essenza SV12","Buggati Bolide W16.4"]
    dict = {"name":name,"list":demo_list}
    return render(request, 'portfolio.html')

def about_input(request):
    all_obj = About.objects.all()
    d_all_obj = {'d':all_obj}
    return render(request, 'admin/about.html', d_all_obj)

def about_insert(request):
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    y_of_exp = request.POST.get('y_of_exp')
    no_of_happy_cus = request.POST.get('no_of_happy_cus')
    no_of_project_finished = request.POST.get('no_of_project_finished')
    no_digital_awards = request.POST.get('no_digital_awards')
    description = request.POST.get('description')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p")

    about_obj = About()
    about_obj.name = name
    about_obj.dob = dob
    about_obj.Phone = phone
    about_obj.email = email
    about_obj.y_of_exp = y_of_exp
    about_obj.no_of_happy_cus = no_of_happy_cus
    about_obj.no_project_finished = no_of_project_finished
    about_obj.no_digital_awards = no_of_project_finished
    about_obj.description = description
    about_obj.date_time = formatted_datetime

    about_obj.save()

    return redirect('about')


def edit_index(request,id):
    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request,'admin/edit.html',d)
