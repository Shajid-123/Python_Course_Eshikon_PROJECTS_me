from django.db import models

class About(models.Model):
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    Phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    y_of_exp = models.CharField(max_length = 500)
    no_of_happy_cus = models.CharField(max_length = 500)
    no_project_finished = models.CharField(max_length=500)
    no_digital_awards = models.CharField(max_length=500)  
    description =  models.TextField(max_length=5000)
    date_time =  models.CharField(max_length=5000)
    v_c = models.CharField(max_length=5000)
    v_status = models.CharField(max_length=10)
    password = models.CharField(max_length=100)



class Companies(models.Model):
    Images = models.ImageField(null=True, blank=True,upload_to="images/")
