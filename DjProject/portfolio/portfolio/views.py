import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from . models import About
from django.contrib import messages
from django.core.signing import Signer
import random
from django.core.mail import send_mail
from django.utils.html import format_html


def demo(request):
    name = "Shoaib Rahman Shajid"
    demo_list = ["Lemborghini Essenza SV12","Buggati Bolide W16.4"]
    dict = {"name":name,"list":demo_list}
    return render(request, 'portfolio.html')

def reg_conf(request):
    return render(request, 'reg_conf.html')


def login(request):
    return render(request, 'login.html')

def login_admin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    log_data = About.objects.get(email = email)
    val = True
    if (log_data.password==password and log_data.v_status == '1'):
        return redirect('about')
    
    elif (log_data.password!=password):
        val = False

    else:
        val = True
    
    msg_dic = {'msg':val}
        
        
    return render(request, 'login.html', msg_dic)
    



def about_input(request):
    all_obj = About.objects.all()
    msg = messages.get_messages(request)
    d_all_obj = {'d':all_obj,'msg':msg}
    return render(request, 'admin/about.html', d_all_obj)

def email_verify(request,id): 
    data = About.objects.get(v_c = id)
    print(id)
    bool_val =  False
    # if data.v_status == 0:
    data.v_status = 1
    data.save()
    bool_val = False
    # else:
    bool_val = True
    bool_dic = {'d':bool_val}
    return render(request,'success.html',bool_dic)

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
    password = request.POST.get('password')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p")
    pattern = r"^[a-zA-Z0-9_.]+@(gmail|yahoo|outlook)\.(com|net|org)$"
    


    if not all([name,dob,phone,email,y_of_exp,no_of_happy_cus,no_digital_awards,description,no_of_project_finished]):
        messages.success(request,"All feilds are required")
    else:
        data = About.objects.all()
        len_data = len(data)
        # if (len_data>=1):
        #     messages.success(request, "You cannnot enter more than one data")
        if not re.match(pattern, email):
            messages.success(request, 'Email is not valid')
        elif (len(phone) != 11):
            messages.success(request, "Phone number is not valid")
        else:
            current_time = datetime.now().strftime("%H:%M:%S")
            h, m, s = map(int, current_time.split(':'))
            t_s = h*3600 + m*60 + s
            random_number = random.choices('1234567890',k=4)
            random_number = ''.join(random_number)
            t_s = str(t_s)
            v_c = t_s+random_number
            encryped_value = Signer().sign(v_c).split(':')[1]
            link = f"<p>Congratulations Mr. {name} ! For registering in our portfolio system. To conform registration</p><a href='http://127.0.0.1:8000/admin/user/email_verification/"+encryped_value+"'target='_blank'>please click this Activation link</a>"
            send_mail(f"Mr. {name} Please conform your Registration - Portfolio panel",encryped_value,'shoaibrahmanshajid@gmail.com',[email],html_message=link)
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
            about_obj.v_c = encryped_value
            about_obj.v_status = 0
            about_obj.password = password


            about_obj.save()
            return redirect('reg_conf')

    return redirect('about')


def edit_index(request,id):
    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request,'admin/edit.html',d)


def about_edit(request):
    
    id = request.POST.get('id')
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

    about_obj = About.objects.get(id=id)
    about_obj.name = name
    about_obj.dob = dob
    about_obj.Phone = phone
    about_obj.email = email
    about_obj.y_of_exp = y_of_exp
    about_obj.no_of_happy_cus = no_of_happy_cus
    about_obj.no_project_finished = no_of_project_finished
    about_obj.no_digital_awards = no_of_project_finished
    about_obj.description = description
    # about_obj.date_time = formatted_datetime

    about_obj.save()

    return redirect('about')

def delete_index(request, id):

    data = About.objects.get(id=id)
    data.delete()
    return redirect('about')