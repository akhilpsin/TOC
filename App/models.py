# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class login_tb(models.Model):
    lid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)

class patient_regis(models.Model):
    pid=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    ph_no=models.IntegerField()
    bld=models.CharField(max_length=30,default="B +ve")
    email=models.CharField(max_length=30)

class presctab(models.Model):
    pid=models.IntegerField()
    docid=models.IntegerField()
    prdate=models.CharField(max_length=300)
    docname=models.CharField(max_length=300,default="Doc")
    pres=models.CharField(max_length=1000)

class labtesttab(models.Model):
    pid=models.IntegerField()
    labid=models.IntegerField()
    prdate=models.CharField(max_length=300)
    tname=models.CharField(max_length=1000)
    result=models.CharField(max_length=1000)
    labname=models.CharField(max_length=300,default="Lab")
    path=models.CharField(max_length=1000)
    
class doctor_regis(models.Model):
    did=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    name=models.CharField(max_length=30)
    specialization=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    experience=models.IntegerField()
    email=models.CharField(max_length=30)
    hid=models.IntegerField()
  
class hosptital_regis(models.Model):
    hid=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    hosp_nm=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    contct_persn=models.CharField(max_length=30)
    contct_no=models.IntegerField()
    email=models.CharField(max_length=30)

class out_hosptital_regis(models.Model):
    hid=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    hosp_nm=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    contct_persn=models.CharField(max_length=30)
    contct_no=models.IntegerField()
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30,default="none")
    password=models.CharField(max_length=30,default="none")

class booking_tb(models.Model):
    #pid=lid(inserted)
    bid=models.IntegerField(primary_key=True)
    pid=models.IntegerField()
    did=models.IntegerField()
    location=models.CharField(max_length=50)
    specialization=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    date=models.DateField()
    hid=models.IntegerField()
    name=models.CharField(max_length=30)
    hosp_name=models.CharField(max_length=50)
    dr_name=models.CharField(max_length=50)
    status=models.CharField(max_length=30)

    

class msgtb(models.Model):
    mid=models.IntegerField(primary_key=True)
    frm_id=models.CharField(max_length=50)
    to_id=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

class testtb(models.Model):
    tid=models.IntegerField(primary_key=True)
    tstname=models.CharField(max_length=50)
    lab_id=models.IntegerField()

class newtesttb(models.Model):
    tid=models.IntegerField(primary_key=True)
    tstname=models.CharField(max_length=50)
    pid=models.IntegerField()
    res=models.CharField(max_length=50,default="none")
    dates=models.CharField(max_length=50,default="none")
    lab_id=models.IntegerField()

class lab_regis(models.Model):
    lab_id=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    lab_nm=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    email=models.CharField(max_length=30)

class out_lab_regis(models.Model):
    lab_id=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    lab_nm=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30,default="none")
    password=models.CharField(max_length=30,default="none")




##    test_nms=models.CharField(max_length=30)
   
class lab_bking(models.Model):
    labbk_id=models.IntegerField(primary_key=True)
    lab_id=models.IntegerField()
    lid=models.IntegerField()
    test_nms=models.CharField(max_length=150)
    bk_time=models.CharField(max_length=30)
    lab_nm=models.CharField(max_length=30)
    date=models.DateField()
    status=models.CharField(max_length=30)
    notifica=models.IntegerField()
    
class med_cat(models.Model):
    med_cid=models.IntegerField(primary_key=True)
    med_cnm=models.CharField(max_length=50)

class medicine_tb(models.Model):
    med_id=models.IntegerField(primary_key=True)
    med_cid=models.IntegerField()
    med_name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=550)
    phar_id=models.IntegerField()

class medpatients(models.Model):
    pid=models.IntegerField()
    medname=models.CharField(max_length=50)
    times=models.CharField(max_length=50)
    prdate=models.CharField(max_length=50)
    noday=models.CharField(max_length=550)
    pharid=models.IntegerField(default=0)


class pharmacy_tb(models.Model):
    phar_id=models.IntegerField(primary_key=True)
    phar_name=models.CharField(max_length=50)
    hid=models.IntegerField()
    lid=models.IntegerField()
    location=models.CharField(max_length=50)

class notifications(models.Model):
    notname=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    pres=models.CharField(max_length=500)


class out_pharmacy_tb(models.Model):
    phar_id=models.IntegerField(primary_key=True)
    phar_name=models.CharField(max_length=50)
    hid=models.IntegerField()
    lid=models.IntegerField()
    location=models.CharField(max_length=50)
    username=models.CharField(max_length=30,default="none")
    password=models.CharField(max_length=30,default="none")

class cart_tb(models.Model):
    cart_id=models.IntegerField(primary_key=True)
    med_name=models.CharField(max_length=50)
    phar_id=models.IntegerField()
    phar_name=models.CharField(max_length=50)
    pid=models.IntegerField()
    name=models.CharField(max_length=30)
    price=models.IntegerField()

class odr_delivry(models.Model):
    odr_id=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    ful_name=models.CharField(max_length=50)
    ph_no=models.IntegerField()
    pay_typ=models.CharField(max_length=30)
    addres=models.TextField()
    billno=models.IntegerField()
    
class odr_details(models.Model):
    ord_dt_id=models.IntegerField(primary_key=True)
    lid=models.IntegerField()
    billno=models.IntegerField()
    med_name=models.CharField(max_length=50)
    phar_id=models.IntegerField()
    phar_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    total=models.IntegerField()
    date=models.DateField()


class chat_tb(models.Model):
    #pid=lid(inserted)
    chatid=models.IntegerField(primary_key=True)
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    did=models.IntegerField()
    time=models.CharField(max_length=30)
    date=models.DateField()
    message=models.TextField()
    lid=models.IntegerField()
    utype=models.CharField(max_length=30)

class diseasetable(models.Model):
    disease=models.CharField(max_length=200)
    symptom1=models.CharField(max_length=200)
    symptom2=models.CharField(max_length=200)
    symptom3=models.CharField(max_length=200)
    symptom4=models.CharField(max_length=200)

class prescriptiontable(models.Model):
    number=models.IntegerField()
    prescription=models.CharField(max_length=200)
    pharmacy=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    userid=models.IntegerField(default=0)
    place=models.CharField(max_length=200,default='0')
    phone=models.IntegerField(default=0)
    name=models.CharField(max_length=30,default='0')


class feedbacktable(models.Model):
    
    feedback=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    lid=models.IntegerField()
    
    
