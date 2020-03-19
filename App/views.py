from django.shortcuts import render
from App.models import *
from django.db.models import Avg, Max, Min, Sum, Count
import json
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core import serializers
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage  
import random
import smtplib
import os
import numpy as np

# Read QR Code
from pyzbar.pyzbar import decode
from PIL import Image
import pyqrcode
import cv2

# Create your views here.
bk_loc=""
bk_hos=""
bk_dist=""
bk_dr=""
bk_dt=""
bk_tym=""
def index_pg(request):
    return render(request,"index.html",{})
def admin_hm_log(request):
    return render(request,"admin_hm_log.html",{})
def Patient_homelog(request):
    return render(request,"Patient_homelog.html",{})
def dhm(request):
    return render(request,"dr_homelog.html",{})
def lab_hmlog(request):
    return render(request,"lab_hmlog.html",{})
def phar_hmlog(request):
    return render(request,"phar_hmlog.html",{})
def articlespg(request):
    return render(request,"indexarticles.html",{})
def migraine(request):
    return render(request,"migraine.html",{})
def apple(request):
    return render(request,"apple.html",{})
def apple(request):
    return render(request,"apple.html",{})
def fever(request):
    return render(request,"Fever in children.html",{})
def top10(request):
    return render(request,"top10.html",{})
def asthma(request):
    return render(request,"asthma.html",{})
def stress(request):
    return render(request,"stress.html",{})
def index(request):
    return render(request,"index.html",{})

def forgot(request):
    a=request.POST.get("user")
    b=request.POST.get("email")
    ob=login_tb.objects.filter(username=a)
    c=""
    d=""
    for i in ob:
        c=i.username
        d=i.password
    email = EmailMessage('Password for your account', 'Your account password is '+str(d), to=[str(b)])
    email.send()
    return HttpResponse("<script>alert('Your password will be sent to your provided email id');window.location.href='/index/';</script>")

def hospital_profile(request):
    print ("hospital_profile")
    if request.session.has_key('uid'):
        us=login_tb.objects.get(lid=request.session['uid'])
        hosp=hosptital_regis.objects.get(lid=request.session['uid'])
        print (request.session['uid'])
        return render(request,"hospital_profile.html",{"hospital":hosp,"userdt":us})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def admin_hospital_vw(request):
    print ("admin_hospital_vw")
    if request.session.has_key('uid'):
        hosp=hosptital_regis.objects.all()
        print (request.session['uid'])
        return render(request,"admin_hospital_vw.html",{"hospital":hosp})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def out_admin_hospital_vw(request):
    print ("admin_hospital_vw")
    if request.session.has_key('uid'):
        hosp=out_hosptital_regis.objects.all()
        print (request.session['uid'])
        return render(request,"out_admin_hospital_vw.html",{"hospital":hosp})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def admin_pharmacy_vw(request):
    print ("admin_pharmacy_vw")
    if request.session.has_key('uid'):
        p=pharmacy_tb.objects.all()
        print (request.session['uid'])
        return render(request,"admin_pharmacy_vw.html",{"pharm":p})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def out_admin_pharmacy_vw(request):
    print ("admin_pharmacy_vw")
    if request.session.has_key('uid'):
        p=out_pharmacy_tb.objects.all()
        print (request.session['uid'])
        return render(request,"out_admin_pharmacy_vw.html",{"pharm":p})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def admin_lab_vw(request):
    print ("admin_lab_vw")
    if request.session.has_key('uid'):
        l=lab_regis.objects.all()
        print (request.session['uid'])
        return render(request,"admin_lab_vw.html",{"labs":l})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def out_admin_lab_vw(request):
    print ("admin_lab_vw")
    if request.session.has_key('uid'):
        l=out_lab_regis.objects.all()
        print (request.session['uid'])
        return render(request,"out_admin_lab_vw.html",{"labs":l})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def admin_patient_vw(request):
    print ("admin_patient_vw")
    if request.session.has_key('uid'):
        p=patient_regis.objects.all()
        print (request.session['uid'])
        return render(request,"admin_patient_vw.html",{"patients":p})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def admin_dr_vw(request):
    print ("admin_dr_vw")
    if request.session.has_key('uid'):
        d=doctor_regis.objects.all()
        print (request.session['uid'])
        return render(request,"admin_dr_vw.html",{"doctors":d})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def admin_home(request):
    print ("for return admin home with windows.location.href")
    if request.session.has_key('uid'):
        user_dt=login_tb.objects.get(lid=request.session['uid'])
        return render(request,"admin_hm.html",{"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def lab_hm(request):
    if request.session.has_key('uid'):
        user_dt=lab_regis.objects.get(lid=request.session['uid'])
        return render(request,"lab_hm.html",{"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def viewlabookings(request):
    print ("viewlabookings")
    if request.session.has_key('uid'):
        user_dt=lab_regis.objects.get(lid=request.session['uid'])
        book=lab_bking.objects.filter(lab_id=user_dt.lab_id)
        return render(request,"viewbookngs.html",{"user_dtt":user_dt,"books":book})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def hosptl_hm(request):
    if request.session.has_key('uid'):
        user_dt=hosptital_regis.objects.get(lid=request.session['uid'])
        us=login_tb.objects.get(lid=request.session['uid'])
        print (request.session['uid'])
        return render(request,"hospital_hm.html",{"user_dtt":user_dt,"uus":us})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def viewpatients(request):
    return render(request,"dr_usvw.html",{})

def checkqr(request):
    print("checkqr")
    s=request.FILES["files"]
    val=""
    if s:
        fs=  FileSystemStorage("App\\static\\res")
        try:
            os.remove("App\\static\\res\\out.png")
        except:
            pass
        fs.save("out.png",s)
        try:
            img = cv2.imread('App\\static\\res\\out.png')

            d = decode(img)
            val=d[0].data.decode('ascii')
           
        except Exception as e:
            print("cannot read",e)
    print("Value: ",val)
    ob=patient_regis.objects.get(lid=int(val))
    return render(request,"dr_userview.html",{"data":ob})
        


        

def dr_hm(request):
    if request.session.has_key('uid'):
        user_dt=doctor_regis.objects.get(lid=request.session['uid'])
        us=login_tb.objects.get(lid=request.session['uid'])
        return render(request,"dr_home.html",{"user_dtt":user_dt,"uus":us})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def dr_Vw_bkngs(request):
    if request.session.has_key('uid'):
        dr_sessn=doctor_regis.objects.get(lid=request.session['uid'])
        book=booking_tb.objects.filter(did=dr_sessn.did)
        return render(request,"dr_vw_bkngs.html",{"books":book})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def pharmacy_hm(request):
    if request.session.has_key('uid'):
        print ("pharmacy_hm")
        user_dt=pharmacy_tb.objects.get(lid=request.session['uid'])
        us=login_tb.objects.get(lid=request.session['uid'])
        return render(request,"phar_hm.html",{"user_dtt":user_dt,"uus":us})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def med_add(request):
    print ("med_add")
    if request.session.has_key('uid'):
        user_dt=pharmacy_tb.objects.get(lid=request.session['uid'])
        med=med_cat.objects.all()
        return render(request,"med_add.html",{"user_dtt":user_dt,"medc":med})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def med_vw(request):
    print ("med_vw")
    if request.session.has_key('uid'):
        user_dt=pharmacy_tb.objects.get(lid=request.session['uid'])
        med=medicine_tb.objects.filter(phar_id=user_dt.phar_id)
        return render(request,"med_vw.html",{"user_dtt":user_dt,"medc":med})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def delete_med(request):
    print ("delete_med")
    data={}
    if request.session.has_key('uid'):        
        id=request.GET.get("id") 
        print ("id",id)
        ob=medicine_tb.objects.get(med_id=int(id))
        ob.delete()
        print ("medicine deleted")
        ob=serializers.serialize("json",medicine_tb.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>") 
def purchase_rep(request):
    print ("purchase_rep")
    if request.session.has_key('uid'):
        user_dt=pharmacy_tb.objects.get(lid=request.session['uid'])
        pharid=user_dt.phar_id
        print ("pharid",pharid)
        book=odr_details.objects.filter(phar_id=pharid)
        return render(request,"phar_pur_reprt.html",{"user_dtt":user_dt,"books":book})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def hospital_dr_bk_vw(request):
    print ("hospital_dr_bk_vw")
    if request.session.has_key('uid'):
        hos=hosptital_regis.objects.get(lid=request.session['uid'])
        user_dt=hosptital_regis.objects.get(lid=request.session['uid'])
        print ("lid",request.session['uid'])
        print ("hos _ id",hos.hid)
        book=booking_tb.objects.filter(hid=hos.hid)
        return render(request,"hospital_dr_bk_vw.html",{"books":book,"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def hosptl_add_phar_hm(request):
    print ("hosptl_add_phar_hm")
    if request.session.has_key('uid'):
        user_dt=hosptital_regis.objects.get(lid=request.session['uid'])
        return render(request,"pharmac_reg_pg_hosp.html",{"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def patient_pg_chat(request):
    print ("patient_pg_chat")
    if request.session.has_key('uid'):
        user=patient_regis.objects.get(lid=request.session['uid'])
        dr=doctor_regis.objects.all()
        print ("patient loged hey")
        return render(request,"patient_chat.html",{"user_dtt":user,"drnm":dr})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def admin_pg_chat(request):
    print ("patient_pg_chat")
    dr=doctor_regis.objects.all()
    lab=lab_regis.objects.all()
    pha=pharmacy_tb.objects.all()
    print ("patient loged hey")
    return render(request,"admin_chat.html",{"user_dtt":"Admin","drnm":dr,"lab":lab,"pha":pha})
##    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def hsp_pg_chat(request):
    print ("patient_pg_chat")
    dr=doctor_regis.objects.filter(hid=request.session['hn'])
    #lab=lab_regis.objects.filter()
    pha=pharmacy_tb.objects.filter(hid=request.session['hn'])
    print ("patient loged hey")
    return render(request,"hsp_chat.html",{"user_dtt":"Admin","drnm":dr,"lab":lab,"pha":pha})

def patient_hm(request):
    print ("for return patient home with windows.location.href")
    if request.session.has_key('uid'):
        user=patient_regis.objects.get(lid=request.session['uid'])
        print ("patient loged hey",request.session['uid'])
        user_dtt=login_tb.objects.get(lid=request.session['uid'])
        return render(request,"Patient_home.html",{"user_dtt":user,"log":user_dtt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")    
def patient_home(request):
    print ("for return patient home with windows.location.href")
    if request.session.has_key('uid'):
        user=patient_regis.objects.get(lid=request.session['uid'])
        print ("patient loged hey",request.session['uid'])
        bk_ststus=booking_tb.objects.filter(pid=request.session['uid'])
        user_dtt=login_tb.objects.get(lid=request.session['uid'])
        print (bk_ststus.count())
        l=bk_ststus.count()
##        l=[]
##        for i in bk_ststus:
##            l.append(i.status)
##        if u'2' in l:
##            print l
##            no=2
        return render(request,"Patient_home.html",{"user_dtt":user,"log":user_dtt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")    
##def notificatn_bkng_tym(request):
##    if request.session.has_key('uid'):
##        obj_update=booking_tb.objects.filter(pid=request.session['uid'])
##        obj_update.status=1
##        obj_update.save()
##        ob=serializers.serialize("json",testtb.objects.filter(pid=request.session['uid']))
##        data["dt1"]=json.loads(ob)
##        print data
##        print "ok"
##        return JsonResponse(data,safe=False)
def lab_home(request):
    print ("lab home")
    if request.session.has_key('uid'):
        user=lab_regis.objects.get(lid=request.session['uid'])
        print ("lab loged hey")
        us=login_tb.objects.get(lid=request.session['uid'])
        return render(request,"lab_hm.html",{"user_dtt":user,"uus":us})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def lab_reg(request):
    if request.session.has_key('uid'):
        return render(request,"lab_reg_pg.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def lab_bk_pg(request):
    if request.session.has_key('uid'):
        return render(request,"labbooking_pg.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def lab_reg_pg_hosp(request):
    if request.session.has_key('uid'):
        user_dt=hosptital_regis.objects.get(lid=request.session['uid'])
        return render(request,"lab_reg_pg_hosp.html",{"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def patient_reg(request):
    print ("in patient_reg")
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("place")
        c=request.POST.get("gender")
        d=request.POST.get("phno")
        e=request.POST.get("email")
        h=request.POST.get("bld")
        f=request.POST.get("username")
        g=request.POST.get("password")
        
        print ("a,b,c,d,e,f,g",a,b,c,d,e,f,g,h)
        obj=login_tb(
                username=f,password=g,usertype="patient"
                )
        obj.save()
        
##        cv2.imshow('generated_png',img)
##        cv2.waitKey(0)
        cnt=login_tb.objects.filter(username=f,password=g)
        print ("phar cnt ",cnt.count())
        if cnt.count()==1:  
            user=login_tb.objects.get(username=f,password=g)
            l_id=user.lid
            print ("l_id===================",l_id)
            msg=str(l_id)
            otptstr= ""
            for i in msg:
                num = ord(i)
                if (num >=0) :
                    if (num <= 127):
                        otptstr= otptstr + i
            msg=otptstr
            print("The Required output is:",msg)
            print(len(msg))
            qr = pyqrcode.create(msg)
            qr.png('App/userqr/'+f+'.png', scale=8)
            img = cv2.imread('App/userqr/'+f+'.png', 0)
            img=cv2.resize(img, (150, 150)) 
            cv2.imwrite('App/userqr/'+f+'.png', img)
            obj=patient_regis(
                lid=l_id,name=a,place=b,gender=c,ph_no=d,email=e,bld=str(h)
                )
            obj.save()
            print ("registered")
            return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")
        else:
            return HttpResponse("<script>alert('User already exist, please register with another username');window.location.href='/index/';</script>")

##    return render(request,"index.html",{})
def booking_hm(request):
    print ("booking_hm from index")
    return render(request,"booking_frm_hm.html",{})
def booking(request):
    print ("booking from patient home")
    if request.session.has_key('uid'):
        user=patient_regis.objects.get(lid=request.session['uid'])
        return render(request,"booking_pg.html",{"user_dt":user})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def pharmacy_pg(request):
    print ("pharmac_reg_pg.html")
    if request.session.has_key('uid'):
        return render(request,"pharmac_reg_pg.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def out_pharmacy_pg(request):
    print ("pharmac_reg_pg.html")
    return render(request,"out_pharmac_reg_pg.html",{})


def hospital_pg(request):
    print ("hospital_pg")
    if request.session.has_key('uid'):
        return render(request,"hosp_reg_pg.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")

def out_hospital_pg(request):
    print ("hospital_pg")
    return render(request,"out_hosp_reg_pg.html",{})

def notices(request):
    print ("notices")
    if request.session.has_key('uid'):
        return render(request,"notice.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def addnotices(request):
    print ("in addnotices")
    if request.method=="POST":
        a=request.POST.get("notname")
        b=request.POST.get("loc")
        c=request.POST.get("desc")
        d=request.POST.get("pres")
        obj=notifications(
                    notname=a,loc=b,desc=c,pres=d
                    )
        obj.save()
        return HttpResponse("<script>alert('Success');window.location.href='/notices/';</script>")

def notivw(request):
    print ("notivw")
    if request.session.has_key('uid'):
        noti=notifications.objects.all()
        return render(request,"notivw.html",{"noti":noti})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
        
def dr_reg(request):
    print ("dr_reg")
    if request.session.has_key('uid'):
        return render(request,"dr_reg.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def hospital_reg(request):
    print ("in hospital_reg")
    if request.session.has_key('uid'):
        if request.method=="POST":
            a=request.POST.get("hosname")
            b=request.POST.get("loc")
            c=request.POST.get("cont_name")
            d=request.POST.get("cont_no")
            e=request.POST.get("email")
            f=request.POST.get("uname")
            g=request.POST.get("pass")
            h=request.POST.get("out")
            print(h)
            if str(h)=="out":
                email = EmailMessage('Status of Registration', 'Your account has been activated. Please login to continue', to=[e])
                email.send()
            print ("a,b,c,d,e,f,g",a,b,c,d,e,f,g)
            obj=login_tb(
                username=f,password=g,usertype="hospital"
                )
            obj.save()
            cnt=login_tb.objects.filter(username=f,password=g)
            print ("phar cnt ",cnt.count())
            if cnt.count()==1:
                user=login_tb.objects.get(username=f,password=g)
                l_id=user.lid
                print ("l_id===================",l_id)
                obj=hosptital_regis(
                    lid=l_id,hosp_nm=a,location=b,contct_persn=c,contct_no=d,email=e
                    )
                obj.save()
                print ("registered")
                return  HttpResponse("<script>alert('Registration Successful');window.location.href='/admin_hm_log/';</script>")
            else:
                 return HttpResponse("<script>alert('User already exist, please register with another username');window.location.href='/pharmacy_regs_admin/';</script>")
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")


def out_hospital_reg(request):
    print ("in hospital_reg")
    if request.method=="POST":
        a=request.POST.get("hosname")
        b=request.POST.get("loc")
        c=request.POST.get("cont_name")
        d=request.POST.get("cont_no")
        e=request.POST.get("email")
        f=request.POST.get("uname")
        g=request.POST.get("pass")
        st=False
        print ("a,b,c,d,e,f,g",a,b,c,d,e,f,g)
        try:
            ob=hosptital_regis.objects.get(hosp_nm=a,location=b,email=e)
        except:
            st=True
        try:
            ob=out_hosptital_regis.objects.get(hosp_nm=a,location=b,contct_persn=c,contct_no=d,email=e)
            
            print ("registered")
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")
        except Exception as ex:
            if st:
                obj=out_hosptital_regis(
                    lid=1,hosp_nm=a,location=b,contct_persn=c,contct_no=d,email=e,username=f,password=g
                    )
                obj.save()
                return  HttpResponse("<script>alert('Registration Successful');window.location.href='/index/';</script>")
            print("Exception: ",ex)
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")
    return HttpResponse("<script>alert('Registration Faild');window.location.href='/index/';</script>")


def lab_regs_pg(request):
    return render(request,"lab_reg_pg.html",{})


def out_lab_regs_pg(request):
    return render(request,"out_lab_reg_pg.html",{})


def lab_regs_fn(request):
    print ("in lab_regs_fn admin")
    if request.session.has_key('uid'):
        if request.method=="POST":
            a=request.POST.get("labname")
            b=request.POST.get("loc")
            c=request.POST.get("uname")
            d=request.POST.get("pass")
            e=request.POST.get("em")
            print ("a,b,c,d,email",a,b,c,d,e)
            obj=login_tb(
                username=c,password=d,usertype="lab"
                )
            obj.save()
            cnt=login_tb.objects.filter(username=c,password=d)
            print ("phar cnt ",cnt.count())
            if cnt.count()==1:
                print ("new user")
                user=login_tb.objects.get(username=c,password=d)
                l_id=user.lid
                print ("l_id===================",l_id)
                obj=lab_regis(
                    lid=l_id,lab_nm=a,location=b,email=e
                    )
                obj.save()
                print ("admin lab registered")
                return HttpResponse("<script>alert('Registration Successful');window.location.href='/admin_hm_log/';</script>")
            else:
                return HttpResponse("<script>alert('User already exist, please register with another username');window.location.href='/pharmacy_regs_admin/';</script>")
        else:
            return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/admin_hm_log/';</script>")
    return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")

def out_lab_regs_fn(request):
    
    if request.method=="POST":
        a=request.POST.get("labname")
        b=request.POST.get("loc")
        c=request.POST.get("uname")
        d=request.POST.get("pass")
        e=request.POST.get("em")
        print ("a,b,c,d,email",a,b,c,d,e)
        try:
            ob=lab_regis.objects.get(lab_nm=a,location=b,email=e)
        except:
            st=True
        try:
            ob=out_lab_regis.objects.get(lab_nm=a,location=b,email=e)
            
            print ("registered")
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")
        except Exception as ex:
            if st:
                obj=out_lab_regis(
                    lid=1,lab_nm=a,location=b,email=e,username=c,password=d
                    )
                obj.save()
                return  HttpResponse("<script>alert('Registration Successful');window.location.href='/index/';</script>")
            print("Exception: ",ex)
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")
    return HttpResponse("<script>alert('Registration Successfull');window.location.href='/index/';</script>")

def lab_regs_fn_hosp(request):
    print ("in lab_regs_fn_hosp---------------")
    if request.method=="POST":
        a=request.POST.get("labname")
        b=request.POST.get("loc")
        c=request.POST.get("uname")
        d=request.POST.get("pass")
        e=request.POST.get("em")
        print ("a,b,c,d,e",a,b,c,d,e)
        obj=login_tb(
                username=c,password=d,usertype="lab"
                )
        obj.save()
        user=login_tb.objects.get(username=c,password=d)
        l_id=user.lid
        print ("l_id===================",l_id)
        obj=lab_regis(
                lid=l_id,lab_nm=a,location=b,email=e
                    )
        obj.save()
        print ("lab registered")
        return HttpResponse("<script>alert('Registration Successful');window.location.href='/hosptl_hm/';</script>")
    else:
        return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/hosptl_hm/';</script>")
def med_insert(request):
    print ("in med_insert---------------")
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("cat")
        c=request.POST.get("descp")
        d=request.POST.get("pric")  
        print ("a,b,c,d",a,b,c,d)
        phar=pharmacy_tb.objects.get(lid=request.session['uid'])
        print ("pharmacy id===================",phar.phar_id,phar.phar_name)
        obj=medicine_tb(
                med_cid=b,med_name=a,price=d,description=c,phar_id=phar.phar_id
                )
        obj.save()
        print ("medicine inserted")
        return HttpResponse("<script>alert('Inserted Successful');window.location.href='/med_add/';</script>")
    else:
        return HttpResponse("<script>alert('Insertion Failed');window.location.href='/pharmacy_hm/';</script>")
def login_check(request):
    print ("in login_check")
    count=0
    if request.method=="POST":
        un=request.POST.get("uname")
        ps=request.POST.get("passwd")
        print ("un",un,"ps",ps)
        user=login_tb.objects.filter(username=un,password=ps)
        print (user)
        count=user.count()
        if count==0:
            print ("Invalid User")
            return HttpResponse("<script>alert('Invalid User');window.location.href='/index/';</script>")
##            return render(request,"index.html",{"msg":"Invalid User"})
        else:
            for i in user:
                typ=i.usertype
                llid=i.lid
            print ("type",typ,"username",un,"paswd",ps,"usercount",count,"userid",llid)
    ##    return render(request,"index.html",{})
            if count==0 or count>1:
                return HttpResponse("<script>alert('Sorry Database Error');window.location.href='/index/';</script>")
##                return render(request,"index.html",{"msg":"Invalid Userdata"})
            if count==1 and typ=="patient":
                print ("patient page")
                user_dt=patient_regis.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                print ("session=: created ",request.session['uid'])
                user_dtt=login_tb.objects.get(lid=request.session['uid'])
                return render(request,"Patient_homelog.html",{"user_dtt":user_dt,"log":user_dtt})
            if count==1 and typ=="admin":
                print ("admin page")
                user_dt=login_tb.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                print ("session=: created ",request.session['uid'])
                hosp=hosptital_regis.objects.all()
                return render(request,"admin_hm_log.html",{"user_dtt":user_dt,"hospital":hosp})
            if count==1 and typ=="hospital":
                print ("hospital page")
                user_dt=hosptital_regis.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                request.session['hn']=user_dt.hid
                print ("session=: created ",request.session['uid'])
                us=login_tb.objects.get(lid=llid)
                return render(request,"hospital_hm.html",{"user_dtt":user_dt,"uus":us})
            if count==1 and typ=="lab":
                print ("lab page")
                user_dt=lab_regis.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                request.session['lid']=user_dt.lab_id
                request.session['lname']=user_dt.lab_nm
                us=login_tb.objects.get(lid=llid)
                print ("session=: created ",request.session['uid'])
                return render(request,"lab_hmlog.html",{"user_dtt":user_dt,"uus":us})
            if count==1 and typ=="doctor":
                print ("doctor page log check")
                user_dt=doctor_regis.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                request.session['did']=user_dt.did
                request.session['dname']=user_dt.name
                print (user_dt.name)
                us=login_tb.objects.get(lid=llid)
                print ("session=: created ",request.session['uid'])
                return render(request,"dr_homelog.html",{"user_dtt":user_dt,"uus":us})
            if count==1 and typ=="pharmacy":
                print ("pharmacy page")
                user_dt=pharmacy_tb.objects.get(lid=llid)
                us=login_tb.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                request.session['ppid']=user_dt.phar_id
                print ("session=: created ",request.session['uid'])
                return render(request,"phar_hmlog.html",{"user_dtt":user_dt,"uus":us})
        return render(request,"index.html",{"msg":"Invalid User"})

def doctor_reg_fn(request):
    print ("in doctor reg fn")
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("speclztn")
        c=request.POST.get("qualiftn")
        d=request.POST.get("exp")
        e=request.POST.get("email")
        f=request.POST.get("uname")
        g=request.POST.get("pass")  
        print ("a,b,c,d,e,f,g",a,b,c,d,e,f,g)
        uchk=login_tb.objects.filter(username=f,password=g)
        if uchk.count()==0:
                obj=login_tb(
                    username=f,password=g,usertype="doctor"
                    )
                obj.save()
                user=login_tb.objects.get(username=f,password=g)
                l_id=user.lid
                print ("l_id===================",l_id)
                user_dt=hosptital_regis.objects.get(lid=request.session['uid'])
                print ("session=: hospital name :",user_dt.hosp_nm,"hospital id",user_dt.hid)
                obj=doctor_regis(
                    lid=l_id,name=a,specialization=b,qualification=c,experience=d,email=e,hid=user_dt.hid
                    )
                obj.save()
                print ("registered")
                llid=request.session['uid']
                return HttpResponse("<script>alert('Registration Successful');window.location.href='/hosptl_hm/';</script>")
        else:
            return HttpResponse("<script>alert('Username already exits,please register with another username');window.location.href='/hosptl_hm/';</script>")

def logout_fn(request):
    try:
        print ("logout_fn")
##        usrtyp=login_tb.objects.all().values_list("usertype",flat=True).distinct()
        if request.session.has_key('uid'):
            print ("session=: deleting ",request.session['uid'])
            del request.session['uid']
            print ("session deleted")
        else:
##            return HttpResponse("plz login")
            return render(request,"index.html",{})
    except Exception as e:
        print ("logout error")
    return render(request,"index.html",{})

def list_hosp(request):
    print ("list_hosp")
    data={}
    loc=request.GET.get("loc")
    print ("District___________________________________________",loc)
    ob=serializers.serialize("json",hosptital_regis.objects.filter(location=loc))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_lab(request):
    print ("list_lab")
    data={}
    loc=request.GET.get("loc")
    print ("District___________________________________________",loc)
    ob=serializers.serialize("json",lab_regis.objects.filter(location=loc))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_phar(request):
    print ("list_phar")
    data={}
    loc=request.GET.get("loc")
    print ("District___________________________________________",loc)
    ob=serializers.serialize("json",pharmacy_tb.objects.filter(location=loc))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_cat(request):
    print ("list_cat")
    data={}
    cat=request.GET.get("catt")
    print ("Categorey___________________________________________",cat)
    ob=serializers.serialize("json",med_cat.objects.all())
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_med(request):
##    print "list_med"
##    data={}
##    cat=request.GET.get("mcat")
##    phar=request.GET.get("phar")
##    print "Categorey_______________________phar____________________",cat,phar
##    ob=serializers.serialize("json",medicine.objects.filter(med_cid=cat))
##    data["dt1"]=json.loads(ob)
##    print data
##    return JsonResponse(data,safe=False)
    print ("list_cat")
    data={}
    catg=request.GET.get("mcat")
    phar=request.GET.get("phar")

    print ("Categorey_____________________pharmacy______________________",catg,phar)
    ob=serializers.serialize("json",medicine_tb.objects.filter(med_cid=catg,phar_id=phar))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_dept(request):
    print ("list_dept")
    data={}
    hosp_id=request.GET.get("hosp_id")
    print ("hospital id___________________________________________",hosp_id)
##    ob =doctor_regis.objects.raw('SELECT distinct(specialization) FROM hms_app_doctor_regis where hid=%s',[hosp_id])
##    print "ob",ob,type(ob)
##    ob=serializers.serialize("json",doctor_regis.objects.raw('SELECT distinct(specialization) FROM hms_app_doctor_regis where hid=%s',[hosp_id]))
##    print ob,"OB--------------------------------------"
    ob=serializers.serialize("json",doctor_regis.objects.filter(hid=hosp_id))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_dr(request):
    print ("list_dr")
    data={}
    dept=request.GET.get("dept")
    hosp_id=request.GET.get("hosp_id")
    print ("selected department id___________________________________________",dept,hosp_id)
    ob=serializers.serialize("json",doctor_regis.objects.filter(specialization=dept,hid=hosp_id))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def list_details(request):
    print ("list_details")
    data={}
    medcn=request.GET.get("medcn")
    print ("selected medcn id___________________________________________",medcn)
    ob=serializers.serialize("json",medicine_tb.objects.filter(med_id=medcn))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def book_now(request):
    print ("in book_now page fn when user not login in")
    if request.method=="POST":
        global bk_loc,bk_hos,bk_dist,bk_dr,bk_dt,bk_tym
        if request.session.has_key('uid'):
            print ("user loged in is",request.session['uid'])
            utype=login_tb.objects.get(lid=request.session['uid'])
            print ("utype.usertype",utype.usertype)
            if utype.usertype=="patient":
                uname=patient_regis.objects.get(lid=request.session['uid'])
                p_nm=uname.name
                print ("p_nm",p_nm)
                global bk_loc,bk_hos,bk_dist,bk_dr,bk_dt,bk_tym
                bk_loc=request.POST.get("loc")
                bk_hos=request.POST.get("selt_hosp")
                bk_dist=request.POST.get("departmnt")
                bk_dr=request.POST.get("dr")
                bk_dt=request.POST.get("appointment_dt")
                bk_tym=request.POST.get("appoint_tym")
                import datetime
                date_str = bk_dt # The date - 29 Dec 2017
                format_str = '%d/%m/%Y' # The format
                datetime_obj = datetime.datetime.strptime(date_str, format_str)
                print(datetime_obj.date())
                bk_dt=str(datetime_obj.date())
                p_nm=uname.name
                print ("bk_loc",bk_loc)
                print ("bk_hos",bk_hos)
                print ("bk_dist",bk_dist)
                print ("bk_dr",bk_dr)
                print ("bk_dt",bk_dt)
                print ("bk_tym",bk_tym)
                check_bk=booking_tb.objects.filter(did=bk_dr,date=bk_dt,time=bk_tym)
                print ("no of bookings",check_bk.count())
                if check_bk.count()<=2:
                    hsp=hosptital_regis.objects.get(hid=bk_hos)
                    dr=doctor_regis.objects.get(did=bk_dr)
                    obj=booking_tb(
                        pid=request.session['uid'],did=bk_dr,location=bk_loc,specialization=bk_dist,time=bk_tym,date=bk_dt,hid=bk_hos,hosp_name=hsp.hosp_nm,dr_name=dr.name,name=p_nm
                        )
                    obj.save()
                    print ("booked")
                    return HttpResponse("<script>alert('Booking Successful');window.location.href='/index/';</script>")
                else:
                    return HttpResponse("<script>alert('Sorry booking closed for this day');window.location.href='/dr_bk_msg/';</script>")
                
            else:
                return HttpResponse("<script>alert('Invalid User, please login');window.location.href='/index/';</script>")            
        else:
            bk_loc=request.POST.get("loc")
            bk_hos=request.POST.get("selt_hosp")
            bk_dist=request.POST.get("departmnt")
            bk_dr=request.POST.get("dr")
            bk_dt=request.POST.get("appointment_dt")
            bk_tym=request.POST.get("appoint_tym")
            print ("bk_loc",bk_loc)
            print ("bk_hos",bk_hos)
            print ("bk_dist",bk_dist)
            print ("bk_dr",bk_dr)
            print ("bk_dt",bk_dt)
            print ("bk_tym",bk_tym)
            return render(request,"login_patient.html",{})
    return render(request,"index.html",{})
def do_booking(request):
    print ("in do_booking fn")
    if request.method=="POST":
        if request.session.has_key('uid'):
            user_dt=patient_regis.objects.get(lid=request.session['uid'])
            print ("user loged in is",request.session['uid'])
            uname=patient_regis.objects.get(lid=request.session['uid'])
            p_nm=uname.name
            print ("p_nm",p_nm)
            bk_loc=request.POST.get("loc")
            bk_hos=request.POST.get("selt_hosp")
            bk_dist=request.POST.get("departmnt")
            bk_dr=request.POST.get("dr")
            bk_dt=request.POST.get("appointment_dt")
            bk_tym=request.POST.get("appoint_tym")
            print ("bk_loc",bk_loc)
            print ("bk_hos",bk_hos)
            print ("bk_dist",bk_dist)
            print ("bk_dr",bk_dr)
            print ("bk_dt",bk_dt)
            print ("bk_tym",bk_tym)
            import datetime
            date_str = bk_dt # The date - 29 Dec 2017
            format_str = '%d/%m/%Y' # The format
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            print(datetime_obj.date())
            bk_dt=str(datetime_obj.date())
            check_bk=booking_tb.objects.filter(did=bk_dr,date=bk_dt,time=bk_tym)
            print ("no of bookings",check_bk.count())
            if check_bk.count()<=2:
                hsp=hosptital_regis.objects.get(hid=bk_hos)
                dr=doctor_regis.objects.get(did=bk_dr)
                obj=booking_tb(
                    pid=request.session['uid'],did=bk_dr,location=bk_loc,specialization=bk_dist,time=bk_tym,date=bk_dt,hid=bk_hos,hosp_name=hsp.hosp_nm,dr_name=dr.name,name=p_nm
                    )
                obj.save()
                print ("booked")
                msgg="booked"
                llid=request.session['uid']
                return HttpResponse("<script>alert('Booked Successful');window.location.href='/dr_bk_msg/';</script>")
            else:
                return HttpResponse("<script>alert('Sorry booking closed for this day');window.location.href='/dr_bk_msg/';</script>")
##            return render(request,"booking_pg.html",{"user_dtt":user_dt,"msg":msgg})
        else:
            return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
    return HttpResponse("<script>alert(' in do booking funtion Please Login');window.location.href='/index/';</script>")
def medicine(request):
    if request.session.has_key('uid'):
        return render(request,"Buymedicine.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def dr_bk_msg(request):
    if request.session.has_key('uid'):
        user_dt=patient_regis.objects.get(lid=request.session['uid'])
        return render(request,"booking_pg.html",{"user_dtt":user_dt})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def book_pg_msg(request):
    return render(request,"booking_pg.html",{})
    
def login_check_after(request):
    print ("in login_check_after")
    count=0
    if request.method=="POST":
        un=request.POST.get("uname")
        ps=request.POST.get("passwd")
        print ("un",un,"ps",ps)
        user=login_tb.objects.filter(username=un,password=ps)
        print (user)
        count=user.count()
        if count==0:
            print ("Invalid User")
            return HttpResponse("<script>alert('Invalid User');window.location.href='/index/';</script>")
        else:
            for i in user:
                typ=i.usertype
                llid=i.lid
            print ("type",typ,"username",un,"paswd",ps,"usercount",count,"userid",llid)
            if count==0 or count>1:
                return render(request,"index.html",{"msg":"Invalid Userdata"})
            if count==1 and typ=="patient":
                print ("patient page")
                global bk_loc,bk_hos,bk_dist,bk_dr,bk_dt,bk_tym
                user_dt=patient_regis.objects.get(lid=llid)
                request.session['uid']=user_dt.lid
                print ("session=: created ",request.session['uid'])
                print ("user loged in is",request.session['uid'])
                uname=patient_regis.objects.get(lid=request.session['uid'])
                p_nm=uname.name
                print ("p_nm",p_nm)

                print ("bk_loc",bk_loc)
                print ("bk_hos",bk_hos)
                print ("bk_dist",bk_dist)
                print ("bk_dr",bk_dr)
                print ("bk_dt",bk_dt)
                print ("bk_tym",bk_tym)
                check_bk=booking_tb.objects.filter(did=bk_dr,date=bk_dt,time=bk_tym)
                print ("no of bookings",check_bk.count())
                if check_bk.count()<=2:
                    print ("check_bk.count()",check_bk.count())
                    hsp=hosptital_regis.objects.get(hid=bk_hos)
                    dr=doctor_regis.objects.get(did=bk_dr)
                    obj=booking_tb(
                        pid=request.session['uid'],did=bk_dr,location=bk_loc,specialization=bk_dist,time=bk_tym,date=bk_dt,hid=bk_hos,hosp_name=hsp.hosp_nm,dr_name=dr.name,name=p_nm
                        )
                    obj.save()
                    print ("booked")
                    bk_loc=""
                    bk_hos=""
                    bk_dist=""
                    bk_dr=""
                    bk_dt=""
                    bk_tym=""
                    print ("global deleted")
                    print ("bk_loc",bk_loc)
                    print ("bk_hos",bk_hos)
                    print ("bk_dist",bk_dist)
                    print ("bk_dr",bk_dr)
                    print ("bk_dt",bk_dt)
                    print ("bk_tym",bk_tym)
                    return HttpResponse("<script>alert('Booked Successful');window.location.href='/dr_bk_msg/';</script>")
                else:
                    return HttpResponse("<script>alert('Sorry booking closed for this day');window.location.href='/dr_bk_msg/';</script>")
                
        return render(request,"index.html",{"msg":"Invalid User"})

def pharmacy_regs_admin(request):
    print ("in pharmacy_regs")
    if request.method=="POST":
        a=request.POST.get("loc")
        b=request.POST.get("uname")
        c=request.POST.get("pass")
        d=request.POST.get("pharname")
        print ("a,b,c,d",a,b,c,d)
        obj=login_tb(
                username=b,password=c,usertype="pharmacy"
                )
        obj.save()
        cnt=login_tb.objects.filter(username=b,password=c)
        print ("phar cnt ",cnt.count())
        if cnt.count()==1:
            user=login_tb.objects.get(username=b,password=c)
            l_id=user.lid
            print ("l_id===================",l_id)
            hhid=0
            obj=pharmacy_tb(
                phar_name=d,lid=l_id,hid=hhid,location=a
                )
            obj.save()
            print ("registered")
            return HttpResponse("<script>alert('Registration Successful');window.location.href='/admin_hm_log/';</script>")
        else:
            return HttpResponse("<script>alert('User already exist, please register with another username');window.location.href='/pharmacy_regs_admin/';</script>")
    else:
        return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/admin_hm_log/';</script>")


def out_pharmacy_regs_admin(request):
    print ("in pharmacy_regs")
    if request.method=="POST":
        a=request.POST.get("loc")
        b=request.POST.get("uname")
        c=request.POST.get("pass")
        d=request.POST.get("pharname")

        try:
            ob=pharmacy_tb.objects.get(phar_name=d,location=a)
        except:
            st=True
        try:
            ob=out_pharmacy_tb.objects.get(phar_name=d,location=a)
            
            print ("registered")
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")
        except Exception as ex:
            if st:
                obj=out_pharmacy_tb(
                    phar_name=d,lid=1,hid=2,location=a,username=b,password=c
                    )
                obj.save()
                return  HttpResponse("<script>alert('Registration Successful');window.location.href='/index/';</script>")
            print("Exception: ",ex)
            return HttpResponse("<script>alert('Registration Faild. Duplicates');window.location.href='/index/';</script>")

    else:
        return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/admin_hm_log/';</script>")


    
def pharmacy_regs_hosp(request):
    print ("in pharmacy_regs hospital")
    if request.method=="POST":
        a=request.POST.get("loc")
        b=request.POST.get("uname")
        c=request.POST.get("pass")
        d=request.POST.get("pharname")
        print ("a,b,c,d",a,b,c,d)
        obj=login_tb(
                username=b,password=c,usertype="pharmacy"
                )
        obj.save()
        cnt=login_tb.objects.filter(username=b,password=c)
        print ("phar cnt ",cnt.count())
        if cnt.count()==1:
            user=login_tb.objects.get(username=b,password=c)
            l_id=user.lid
            print ("l_id===================",l_id)
            hhid=hosptital_regis.objects.get(lid=request.session['uid'])
            print ("hos id",hhid.hid)
            obj=pharmacy_tb(
                phar_name=d,lid=l_id,hid=hhid.hid,location=a
                )
            obj.save()
            print ("registered")
            return HttpResponse("<script>alert('Registration Successful');window.location.href='/hosptl_hm/';</script>")
        else:
            return HttpResponse("<script>alert('User already exist, please register with another username');window.location.href='/pharmacy_regs_hosp/';</script>")
    else:
        return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/hosptl_hm/';</script>")

#----------------------------------Medicine---------------------------------
def medicine(request):
    if request.session.has_key('uid'):
        return render(request,"Buymedicine.html",{})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def vw_cart(request):
    print ("in vw_cart")
    if request.session.has_key('uid'):
        usrid=request.session['uid']
        my_cart=cart_tb.objects.filter(pid=usrid)
        print ("no of items",my_cart.count())
        no_items=my_cart.count()
        return render(request,"view_cart.html",{"cart_items":my_cart,"itemcount":no_items})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def vw_cart_order(request):
    print ("in vw_cart_order")
    if request.session.has_key('uid'):
        usrid=request.session['uid']
        my_order=odr_details.objects.filter(lid=usrid)
        print ("no of orders",my_order.count())
        no_items=my_order.count()
        return render(request,"Patient_order_vw.html",{"cart_items":my_order,"itemcount":no_items})
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def update_cart(request):
    print ("in update_cart")
    if request.session.has_key('uid'):
        usrid=request.session['uid']
        my_cart=cart_tb.objects.filter(pid=usrid)
        print ("no of items",my_cart.count())
        no_items=my_cart.count()
        return render(request,"view_cart.html",{"cart_items":my_cart,"itemcount":no_items})
def add_cart(request):
    print ("add_cart")
    if request.method=="POST":
        a=request.POST.get("medc_nm")
        b=request.POST.get("sel_phar_nm")
        c=request.POST.get("pric")
        d=request.session['uid']
        print ("med id,phar id,price,patient id ",a,b,c,d)
        m_nm=medicine_tb.objects.get(med_id=a)
        print (m_nm.med_name)
        p_nm=pharmacy_tb.objects.get(phar_id=b)
        print (p_nm.phar_name)
        pat_nm=patient_regis.objects.get(lid=request.session['uid'])
        obj=cart_tb(
                med_name=m_nm.med_name,phar_id=b,phar_name=p_nm.phar_name,pid=request.session['uid'],name=pat_nm.name,price=c
                )
        obj.save()
        print ("added to cart")
        return HttpResponse("<script>alert('added to cart Successful');window.location.href='/medicine/';</script>")
    else:
        return HttpResponse("<script>alert('Registration Unsuccessful');window.location.href='/index/';</script>")

import webbrowser
def delete_pdt(request):
    print ("delete_pdt")
    if request.session.has_key('uid'):
        itid=request.GET.get("itid") 
        print ("itid",itid)
        ob=cart_tb.objects.get(cart_id=itid)
        ob.delete()
        print ("deleted")
        usrid=request.session['uid']
        my_cart=cart_tb.objects.filter(pid=usrid)
        print ("no of items",my_cart.count())
        no_items=my_cart.count()
        return HttpResponse("<script>alert('Delete from cart');window.location.href='/vw_cart/';</script>")
    else:
        return render(request,"index.html",{"msg":"Invalid User"})
##    return render(request,"view_cart.html",{"cart_items":my_cart,"itemcount":no_items})
##    data={}
##    ob=serializers.serialize("json",product_tb.objects.all())
##    data["dt1"]=json.loads(ob)
##    print data
##    return JsonResponse(data,safe=False)
##    return HttpResponse("deleted")
def cart_sum(request):
    print ("not used--------------------------------------------------")
    print (cart_sum)
    return HttpResponse("<script>alert('quantity added');window.location.href='/update_cart/';</script>")
def placeorder(request):
    print ("in placeorder")
    if request.method=="POST":
        bilno=''
        for i in range(10):
            n=random.randrange(0,9)
            bilno=bilno+str(n)
        print ("bilno",bilno)
        a=request.POST.get("funame")
        b=request.POST.get("mob")
        c=request.POST.get("adr")
        d=request.POST.get("phname")
        e=request.POST.get("qunt")
        f=request.POST.get("pdtnm")
        g=request.POST.get("prcc")
        print ("a,b,c,d,e,f,g",a,b,c,d,e,f,g)
        phar_list=((str(d).replace("u+",''))).replace("+",'').split(",")
        print ("length",len(phar_list))
        arylen=len(phar_list)/2
        print ("arylen",arylen)
        qu_list=((str(e).replace("u+",''))).replace("+",'').split(",")
        pdt_list=((str(f).replace("u+",''))).replace("+",'').split(",")
        pr_list=((str(g).replace("u+",''))).replace("+",'').split(",")
        print ("phar_list-------",phar_list)
        print ("qu_list---------",qu_list)
        print ("(pdt_list--------",pdt_list)
        print ("pr_list---------",pr_list)
        dy=datetime.now().strftime("%Y-%m-%d")
        print ("date",dy)  
        obj=odr_delivry(
                lid=request.session['uid'],ful_name=a,ph_no=b,pay_typ="COD",addres=c,billno=int(bilno)
                )
        obj.save()
        for i in range(0,len(phar_list)-1):
            print (i)
            pharid=pharmacy_tb.objects.get(phar_name=phar_list[i])
            print ("paharmy id",pharid.phar_id)
            phrid=pharid.phar_id
            tot=int(qu_list[i]) * int(pr_list[i])
            print ("tot",tot)
            obj1=odr_details(
                lid=request.session['uid'],billno=int(bilno),med_name=pdt_list[i],phar_id=int(phrid),phar_name=phar_list[i],quantity=int(qu_list[i]),price=int(pr_list[i]),total=tot,date=dy
                )
            obj1.save()
            print ("inserted")
        ob=cart_tb.objects.filter(pid=request.session['uid'])
        ob.delete()
        print ("deleted from cart")
    return HttpResponse("<script>alert('Medicine Ordered Successfully');window.location.href='/patient_home/';</script>")
#---------------------------------------lab booking--------------------------------------------------------------------------

def book_lab(request):
    print ("booking lab")
    if request.method=="POST":
        if request.session.has_key('uid'):
            print ("user loged in is",request.session['uid'])
            utype=login_tb.objects.get(lid=request.session['uid'])
            print ("utype.usertype",utype.usertype)

                   
            if utype.usertype=="patient":
                bk_tstnm=''
                bk_loc=request.POST.get("loc")
                bk_lab=request.POST.get("selt_lab")
                bk_tsts=request.POST.get("tstname")
                bk_tym=request.POST.get("bok_tym")
                bk_dt=request.POST.get("appointment_dt")
                print (type(bk_tsts))
                asciistring = bk_tsts.encode("ascii")
                print (type(asciistring))
                print (asciistring,"-----------------------------------------------------")
                tlsst=asciistring.split(",")
                print ("----------",tlsst)
                for i in tlsst:
                    t=testtb.objects.get(tid=int(i))
                    bk_tstnm=bk_tstnm+t.tstname+","
##                print type(bk_tstnm),bk_tstnm[:-1]
                bk_tsts=bk_tstnm[:-1]
                print (bk_tsts)
                print ("bk_loc",bk_loc)
                print ("bk_lab",bk_lab)
                print ("bk_tsts",bk_tsts)
                print ("bk_tym",bk_tym)
                print ("bk_dt",bk_dt)
                lbnm=lab_regis.objects.get(lab_id=bk_lab)
                obj=lab_bking(
                    lab_id=bk_lab,lid=request.session['uid'],test_nms=bk_tsts,bk_time=bk_tym,lab_nm=lbnm.lab_nm,date=bk_dt,status="requested",notifica=1
                    )
                obj.save()
                print ("lab booked")
                return HttpResponse("<script>alert('Lab Booked Successfully');window.location.href='/patient_home/';</script>")
            else:
                return HttpResponse("not a registered patient")
    return HttpResponse("<script>alert('not booked');window.location.href='/patient_home/';</script>")
#--------------------------------booking views patient--------------------------------------------------------
def dr_bk_vw(request):
    print ("dr bking vw")
    book=booking_tb.objects.filter(pid=request.session['uid'])
    return render(request,"Patient_dr_bk_vw.html",{"books":book})

def lab_bk_vw(request):
    print ("lab bking vw")
    book=lab_bking.objects.filter(lid=request.session['uid'])
    return render(request,"Patient_lab_bk_vw.html",{"books":book})
#--------------------------------update booking time--------------------------------------------------------
def updt_bkng_tym(request):
    print ("updt_bkng_tym")
    if request.method=="POST":
        pidd=request.POST.get("pidd")
        appoint_tym=request.POST.get("appoint_tym")
        pptnnm=request.POST.get("pptnnm")
        pswd=request.POST.get("pswd")
        dttt=request.POST.get("dttt")
        bkid=request.POST.get("bkkidd")
        print ("pidd,appoint_tym,pptnnm,pswd,bkid",pidd.strip(),appoint_tym.strip(),pptnnm.strip(),pswd.strip(),dttt.strip(),bkid.strip())
        obj_update=booking_tb.objects.get(bid=int(bkid))
        obj_update.time=appoint_tym.strip()
        obj_update.status=2
        obj_update.save()
        password=pswd.strip()
        ptdt=patient_regis.objects.get(lid=int(pidd))
        pn=ptdt.name
        print (pn)
        tosend=ptdt.email
        print (tosend)
        drdt=doctor_regis.objects.get(lid=request.session['uid'])
        frmsend=drdt.email
        print (frmsend)
        msg=str("Sorry "+pn+", Your appointment time on "+dttt.strip()+ " change to "+appoint_tym.strip())
        print (msg)

##        server=smtplib.SMTP('smtp.gmail.com',587)
##        server.ehlo()
##        server.starttls()
##        server.login(frmsend,password)
##        server.sendmail(frmsend,tosend,msg)
##        server.close()  
        return HttpResponse("<script>alert('Successfully Changed. Notification to patient will be send');window.location.href='/dr_Vw_bkngs/';</script>")
    return HttpResponse("<script>alert('Mail Send Unsuccessfully');window.location.href='/dr_Vw_bkngs/';</script>")
def updt_lab_bkng_tym(request):
    print ("updt_lab_bkng_tym")
    if request.method=="POST":
##        pidd=request.POST.get("pidd")
        bkidd=request.POST.get("bkidd")
        appoint_tym=request.POST.get("appoint_tym")
        bkngstatus=request.POST.get("bkstatus")
        dttt=request.POST.get("dttt")
        pswd=request.POST.get("pswd")
##        pswd=request.POST.get("pswd")
        print ("pidd,bkidd",bkidd.strip())
        print ("appoint_tym",appoint_tym)
        print ("bkngstatus",bkngstatus)
        print ("dttt",dttt.strip())
        print ("password",pswd)
        pemil=lab_bking.objects.get(labbk_id=int(bkidd))
        emil=patient_regis.objects.get(lid=pemil.lid)
        tosend=emil.email
        lb=lab_regis.objects.get(lab_id=pemil.lab_id)
        frmsend=lb.email
        print (tosend,frmsend)
        pn=emil.name
        lnm=lb.lab_nm
##        nwtym=bkidd.strip()
##        nwstatus=bkngstatus.strip()
##        print "nwtym,nwstatus",nwtym,nwstatus
        obj_update=lab_bking.objects.get(labbk_id=bkidd)
        obj_update.bk_time=appoint_tym
        obj_update.status=bkngstatus
        obj_update.notifica=2
        obj_update.save()
        print ("updated")
        msg=str("Dear " +pn+", Your "+lnm+" lab appointment  on "+dttt.strip()+ " at "+appoint_tym.strip()+ " was "+bkngstatus)
        print (msg)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(frmsend,pswd)
        server.sendmail(frmsend,tosend,msg)
        server.close() 
        return HttpResponse("<script>alert('Booking Updated and notification mail send Successfully');window.location.href='/viewlabookings/';</script>")
    return HttpResponse("<script>alert('Booking has no change');window.location.href='/viewlabookings/';</script>")
def addtest(request):
    print ("addtest")
    user_dt=lab_regis.objects.get(lid=request.session['uid'])
    users=patient_regis.objects.all()
    return render(request,"addtest.html",{"user_dtt":user_dt,"data":users})
def del_test(request):
    print ("del_test")
    user_dt=lab_regis.objects.get(lid=request.session['uid'])
    test_dt=testtb.objects.filter(lab_id=user_dt.lab_id)
    return render(request,"deltest.html",{"tests":test_dt,"user_dtt":user_dt})
def deleting_test(request):
    print ("deleting_test")
    if request.session.has_key('uid'):        
        user_dt=lab_regis.objects.get(lid=request.session['uid'])
        test_dt=testtb.objects.filter(lab_id=user_dt.lab_id)
        tst=request.POST.get("tst") 
        print ("tst",tst)
        ob=testtb.objects.get(tid=tst)
        ob.delete()
        print ("deleted")
        return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/del_test/';</script>")
    return HttpResponse("<script>alert('Please Login');window.location.href='/index/';</script>")
def addingtest(request):
    print ("addingtest")
    if request.method=="POST":
        print ("in addingtest post function")
        testname=request.POST.get("testname")
        pid=request.POST.get("username")
        res=request.POST.get("res")
        from datetime import datetime

        dat=datetime.today().strftime('%d/%m/%Y')
        print ("testname",testname,pid)
        lab=lab_regis.objects.get(lid=request.session['uid'])
        lbnm=lab.lab_id
        obj=testtb(
                tstname=testname,lab_id=lbnm
                )
        obj.save()
        obj1=newtesttb(
                tstname=testname,lab_id=lbnm,pid=int(pid),dates=str(dat),res=str(res)
                )
        obj1.save() 
        return HttpResponse("<script>alert('Added  Successfully');window.location.href='/addtest/';</script>")
    return HttpResponse("<script>alert('Insertion Failed');window.location.href='/addtest/';</script>")


glpid,glname,glplace,glphno,glemail="","","","",""

def showpdf(request):
    global glpid,glname,glplace,glphno,glemail
    pdfpath=request.POST.get("path")
    webbrowser.open(pdfpath)
    ob=newtesttb.objects.filter(pid=int(glpid))
    md=medpatients.objects.filter(pid=int(glpid))
    lb=labtesttab.objects.filter(pid=int(glpid))
    pr=presctab.objects.filter(pid=int(glpid))
    
    try:
        ob1=medicine_tb.objects.filter(phar_id=int(request.session['ppid']))
    except:
        ob1=medicine_tb.objects.filter(phar_id=0)
    return render(request,"dr_usertests.html",{"data":ob,"email":glemail,"phno":glphno,"place":glplace,"name":glname,"pid":glpid,"phar":ob1,"med":md,"doc":pr,"lab":lb})
    

def viewtests(request):
    global glpid,glname,glplace,glphno,glemail
    pid=request.POST.get("pid")
    name=request.POST.get("name")
    place=request.POST.get("place")
    phno=request.POST.get("phno")
    email=request.POST.get("email")
    glpid,glname,glplace,glphno,glemail=pid,name,place,phno,email
    ob=newtesttb.objects.filter(pid=int(pid))
    md=medpatients.objects.filter(pid=int(pid))
    lb=labtesttab.objects.filter(pid=int(pid))
    pr=presctab.objects.filter(pid=int(pid))
    
    try:
        ob1=medicine_tb.objects.filter(phar_id=int(request.session['ppid']))
    except:
        ob1=medicine_tb.objects.filter(phar_id=0)
    return render(request,"dr_usertests.html",{"data":ob,"email":email,"phno":phno,"place":place,"name":name,"pid":pid,"phar":ob1,"med":md,"doc":pr,"lab":lb})

def addpresc(request):
    pid=request.POST.get("pid")
    d=request.POST.get("date")
    pre=request.POST.get("presc")
    ob=presctab(pid=int(pid),prdate=d,pres=pre,docid=int(request.session['did']),docname=request.session['dname']).save()
    return render(request,"dr_homelog.html",{})

def testres(request):
    s = request.FILES["myfile"]
    print (s)
    if request.FILES["myfile"]:
        fs = FileSystemStorage("App/static/files/")
        fs.save(s.name, s)
        filename ="App/static/files/"+s.name
        pid=request.POST.get("pid")
        d=request.POST.get("date")
        name=request.POST.get("name")
        res=request.POST.get("res")
        ob=labtesttab(pid=int(pid),prdate=d,tname=name,labname=request.session['lname'],labid=int(request.session['lid']),result=res,path=filename).save()
    return render(request,"dr_homelog.html",{})

def medpat(request):
    pid=request.POST.get("pid")
    d=request.POST.get("date")
    name=request.POST.get("medname")
    t=request.POST.get("time")
    dys=request.POST.get("days")
    ob=medpatients(pid=int(pid),prdate=d,medname=name,pharid=int(request.session['ppid']),times=t,noday=dys).save()
    return render(request,"dr_homelog.html",{})

    
def pharmviewtests(request):
    pid=request.POST.get("pid")
    name=request.POST.get("name")
    place=request.POST.get("place")
    phno=request.POST.get("phno")
    email=request.POST.get("email")
    ob=newtesttb.objects.filter(pid=int(pid))
    return render(request,"pharm_usertests.html",{"data":ob,"email":email,"phno":phno,"place":place,"name":name})
    


def fetchtest(request):
    print ("fetchtest")
    data={}
    labid=request.GET.get("tsts")
    print ("labid",labid)
    ob=serializers.serialize("json",testtb.objects.filter(lab_id=labid))
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)
def chatting(request):
    print ("chatting")
    if request.session.has_key('uid'):
        user=patient_regis.objects.get(lid=request.session['uid'])
        msg=request.POST.get("msgg")
        drid=request.POST.get("ppid")
        print ("message___________________________________________",msg)
        print ("doctor___________________________________________",drid)

        usr=patient_regis.objects.get(lid=request.session['uid'])
        usrtyp=login_tb.objects.get(lid=request.session['uid'])
        tm=datetime.now().strftime("%H:%M:%S")
        print ("time",tm)
        dy=datetime.now().strftime("%Y-%m-%d")
        print ("date",dy)        
        obj=chat_tb(
            pid=usr.pid,pname=usr.name,did=drid,time=tm,date=dy,message=msg,lid=request.session['uid'],utype=usrtyp.usertype
            )
        obj.save()
        print ("message saved")
##        drid=doctor_regis.objects.get(lid=request.session['uid'])
        fetmsg=chat_tb.objects.filter(did=drid,pid=usr.pid)
        print ("fetmsg",fetmsg.count())
        return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":drid})

#------------------------------------------------------------------------        
        return render(request,"patient_chat.html",{"user_dtt":user,"drnm":dr})
def vwchatwithdr(request):
    print ("vwchatwithdr")
    if request.method=="POST":
        iddr=request.POST.get("iddr")
        print ("doctor id",iddr,"pip------- lid",request.session['uid'])
        pn=patient_regis.objects.get(lid=request.session['uid'])
        fetmsg=chat_tb.objects.filter(pid=pn.pid,did=int(iddr))
        print ("fetmsg",fetmsg.count())
        return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":iddr})
    return HttpResponse("no messages")

def vwchat_new(request):
    print ("vwchatwithdr")
    if request.method=="POST":
        iddr=request.POST.get("iddr")
        print ("doctor id",iddr,"pip------- lid",request.session['uid'])
        fetmsg={}
        try:
            pn=doctor_regis.objects.get(lid=request.session['uid'])
            fetmsg=chat_tb.objects.filter(pid=pn.pid,did=int(iddr))
            print ("fetmsg",fetmsg.count())
            return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":iddr})
        except:
            pass
        try:
            pn=lab_regis.objects.get(lid=request.session['uid'])
            fetmsg=chat_tb.objects.filter(pid=pn.pid,did=int(iddr))
            print ("fetmsg",fetmsg.count())
            return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":iddr})
        except:
            pass
        try:
            pn=patient_regis.objects.get(lid=request.session['uid'])
            fetmsg=chat_tb.objects.filter(pid=pn.pid,did=int(iddr))
            print ("fetmsg",fetmsg.count())
            return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":iddr})
        except:
            pass
        try:
            pn=pharmacy_tb.objects.get(lid=request.session['uid'])
            fetmsg=chat_tb.objects.filter(pid=pn.pid,did=int(iddr))
            print ("fetmsg",fetmsg.count())
            return render(request,"patient_vw_chat.html",{"chatmsg":fetmsg,"did":iddr})
        except:
            pass
        
    return HttpResponse("no messages")


def patients_msgto_dr(request):
    print ("patients_msgto_dr")
    if request.session.has_key('uid'):
        user=doctor_regis.objects.get(lid=request.session['uid'])
        fetmsg=chat_tb.objects.filter(did=user.did)
        print ("fetmsg",fetmsg.count())
        return render(request,"msgstodr.html",{"chatmsg":fetmsg})
    return HttpResponse("no messages")
def msgfrm_p(request):
    print ("msgfrm_p")
    if request.method=="POST":
        selt_pn=request.POST.get("selt_pn")
        print ("selt_pn",selt_pn)
        drid=doctor_regis.objects.get(lid=request.session['uid'])
        fetmsg=chat_tb.objects.filter(did=drid.did,pid=int(selt_pn))
        print ("fetmsg",fetmsg.count())
        return render(request,"dr_vw_chat.html",{"chatmsg":fetmsg,"pid":selt_pn})
    return HttpResponse("no messages")
def sendrply(request):
    print ("sendrply")
    if request.session.has_key('uid'):
        user=doctor_regis.objects.get(lid=request.session['uid'])
        print ("sendrply chatting print")
#------------------------------------chatting----------------------------
        msg=request.POST.get("msgg")
        ppid=request.POST.get("ppid")
        print ("message___________________________________________",msg)
        print ("patient___________________________________________",ppid)
        pn=patient_regis.objects.get(pid=ppid)
        usr=doctor_regis.objects.get(lid=request.session['uid'])
        usrtyp=login_tb.objects.get(lid=request.session['uid'])
        
        tm=datetime.now().strftime("%H:%M:%S")
        print ("time",tm)
        dy=datetime.now().strftime("%Y-%m-%d")
        print ("date",dy)        
        obj=chat_tb(
            pid=ppid,pname=pn.name,did=usr.did,time=tm,date=dy,message=msg,lid=request.session['uid'],utype=usrtyp.usertype
            )
        obj.save()
        print ("message saved")
        drid=doctor_regis.objects.get(lid=request.session['uid'])
        fetmsg=chat_tb.objects.filter(did=drid.did,pid=int(ppid))
        print ("fetmsg",fetmsg.count())
        return render(request,"dr_vw_chat.html",{"chatmsg":fetmsg,"pid":ppid})
    return HttpResponse("chat  failed")
#------------------------------------profile updation----------------------------
def hosp_prof_up(request):
    print ("hosp_prof")
    if request.method=="POST":
        if request.session.has_key('uid'):
            a=request.POST.get("hosname")
            b=request.POST.get("uname")
            c=request.POST.get("cont_name")
            d=request.POST.get("cont_no")
            e=request.POST.get("email")
            f=request.POST.get("pass")
            print ("profile details",a,b,c,d,e,f)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=b
            obj_update.password=f
            obj_update.save()
            print ("updated1")
            obj_update1=hosptital_regis.objects.get(lid=request.session['uid'])
            obj_update1.hosp_nm=a
            obj_update1.contct_persn=c
            obj_update1.contct_no=d
            obj_update1.email=e
            obj_update1.save()
            print ("updated2")            
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/hospital_profile/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def patient_prof_up(request):
    print ("patient_prof_up")
    if request.method=="POST":
        if request.session.has_key('uid'):
            a=request.POST.get("name")
            b=request.POST.get("em")
            c=request.POST.get("gender")
            d=request.POST.get("ph_no")
            e=request.POST.get("uname")
            f=request.POST.get("pass")
            print ("profile details",a,b,c,d,e,f)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=e
            obj_update.password=f
            obj_update.save()
            print ("updated1")
            obj_update1=patient_regis.objects.get(lid=request.session['uid'])
            obj_update1.name=a
            obj_update1.email=b
            obj_update1.gender=c
            obj_update1.ph_no=d
            obj_update1.save()
            print ("updated2")            
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/patient_hm/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def phar_prof_up(request):
    print ("phar_prof_up")
    if request.method=="POST":
        if request.session.has_key('uid'):
            a=request.POST.get("name")
            b=request.POST.get("uname")
            c=request.POST.get("pass")
            print ("profile details",a,b,c)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=b
            obj_update.password=c
            obj_update.save()
            print ("updated1")
            obj_update1=pharmacy_tb.objects.get(lid=request.session['uid'])
            obj_update1.name=a
            obj_update1.save()
            print ("updated2")            
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/pharmacy_hm/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def dr_prof_up(request):
    print ("dr_prof_up")
    if request.method=="POST":
        if request.session.has_key('uid'):
            a=request.POST.get("name")
            b=request.POST.get("email")
            d=request.POST.get("uname")
            c=request.POST.get("pass")
            print ("profile details",a,b,c)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=d
            obj_update.password=c
            obj_update.save()
            print ("updated1")
            obj_update1=doctor_regis.objects.get(lid=request.session['uid'])
            obj_update1.name=a
            obj_update1.email=b
            obj_update1.save()
            print ("updated2")            
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/dr_hm/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def lab_prof_up(request):
    print ("lab_prof_up")
    if request.method=="POST":
        if request.session.has_key('uid'):
            a=request.POST.get("name")
            b=request.POST.get("email")
            d=request.POST.get("uname")
            c=request.POST.get("pass")
            print ("profile details",a,b,c)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=d
            obj_update.password=c
            obj_update.save()
            print ("updated1")
            obj_update1=lab_regis.objects.get(lid=request.session['uid'])
            obj_update1.lab_nm=a
            obj_update1.email=b
            obj_update1.save()
            print ("updated2")            
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/lab_home/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def admin_prof_up(request):
    print ("admin_prof_up")
    if request.method=="POST":
        if request.session.has_key('uid'):
            d=request.POST.get("uname")
            c=request.POST.get("pass")
            print ("profile details",d,c)
            obj_update=login_tb.objects.get(lid=request.session['uid'])
            obj_update.username=d
            obj_update.password=c
            obj_update.save()
            print ("updated1")       
        return HttpResponse("<script>alert('Profile updated successfully');window.location.href='/admin_home/';</script>")
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
#---------------------------delete--------------------
def delete_hos(request):
    print ("delete_hos")
    data={}
    if request.session.has_key('uid'):        
        hid=request.GET.get("hid") 
        print ("hid",hid)
        ob=hosptital_regis.objects.get(hid=int(hid))
        ob.delete()
        print ("Hospital deleted")
        ob=serializers.serialize("json",hosptital_regis.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")     
def delete_phar(request):
    print ("delete_phar")
    data={}
    if request.session.has_key('uid'):        
        id=request.GET.get("id") 
        print ("id",id)
        ob=pharmacy_tb.objects.get(phar_id=int(id))
        ob.delete()
        print ("Pharmacy deleted")
        ob=serializers.serialize("json",pharmacy_tb.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>")
def delete_lab(request):
    print ("delete_lab")
    data={}
    if request.session.has_key('uid'):        
        id=request.GET.get("id") 
        print ("id",id)
        ob=lab_regis.objects.get(lab_id=int(id))
        ob.delete()
        print ("lab deleted")
        ob=serializers.serialize("json",lab_regis.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>") 
def delete_patient(request):
    print ("delete_patient")
    data={}
    if request.session.has_key('uid'):        
        id=request.GET.get("id") 
        print ("id",id)
        ob=patient_regis.objects.get(pid=int(id))
        ob.delete()
        print ("patient deleted")
        ob=serializers.serialize("json",patient_regis.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>") 
def delete_dr(request):
    print ("delete_dr")
    data={}
    if request.session.has_key('uid'):        
        id=request.GET.get("id") 
        print ("id",id)
        ob=doctor_regis.objects.get(did=int(id))
        ob.delete()
        print ("dr deleted")
        ob=serializers.serialize("json",doctor_regis.objects.all())
        data["dt1"]=json.loads(ob)
        print (data)
        return JsonResponse(data,safe=False)
    return HttpResponse("<script>alert('please login');window.location.href='/index/';</script>") 


#disease prediction
def disease(request):
    return render(request,'adminadddisease.html',{})

#add disease by admin
def adddisease(request):
    disease=request.POST.get("disease")
    symptom1=request.POST.get("symptom1")
    symptom2=request.POST.get("symptom2")
    symptom3=request.POST.get("symptom3")
    symptom4=request.POST.get("symptom4")
    s1=symptom1.lower()
    s2=symptom2.lower()
    s3=symptom3.lower()
    s4=symptom4.lower()
    d=disease.lower()
    
    print ("symptom1",s1)
    print ("symptom2",s2)
    print ("symptom3",s3)
    print ("symptom4",s4)
    print ("disease",d)
    obj=diseasetable(disease=disease,symptom1=symptom1,symptom2=symptom2,symptom3=symptom3,symptom4=symptom4)
    obj.save()
    return HttpResponse("<script>alert('Successfully Added');window.location.href='/disease/'</script>")

def viewdiseasepage(request):

    return render(request,'symptoms.html',{})

def healthcheck(request):
    symptom1=request.POST.get("symptom1")
    symptom2=request.POST.get("symptom2")
    symptom3=request.POST.get("symptom3")
    symptom4=request.POST.get("symptom4")
    s1=symptom1.lower()
    s2=symptom2.lower()
    s3=symptom3.lower()
    s4=symptom4.lower()
    
    print ("symptom1",s1)
    print ("symptom2",s2)
    print ("symptom3",s3)
    print ("symptom4",s4)
    obj=diseasetable.objects.filter(symptom1=s1,symptom2=s2,symptom3=s3,symptom4=s4)
    c=obj.count()
    if c==1:
        obj=diseasetable.objects.get(symptom1=s1,symptom2=s2,symptom3=s3,symptom4=s4)
        disease=obj.disease
        result="<div style='height: 117px;width: 400px;background-color:#00f9ff;color: white;font-size: 50px;text-transform: capitalize;margin: auto;margin-top: 15%;padding: 39px 21px 10px 82px;'>"+disease+"</div>"
        return HttpResponse(result)
    else:
        return HttpResponse("<script>alert('No Disease Found');window.location.href='/viewdiseasepage/'</script>")
    

def prescription(request):
     obj=pharmacy_tb.objects.all()
     return render(request,'prescription.html',{'detail':obj})

def uploadprescription(request):
    uid=request.session['uid']
    number=request.POST.get("number")
    prescription=request.FILES["prescription"]
    pharmacy=request.POST.get("pharmacy")
    print ("pharmacy",pharmacy)
    print ("prescription",prescription)
    print ("number",number)
    status="Pending"
    obj1=patient_regis.objects.get(lid=uid)
    place=obj1.place
    phone=obj1.ph_no
    name=obj1.name
    fs=FileSystemStorage("hms_app/static/prescription")
    fs.save(prescription.name,prescription)
    obj=prescriptiontable(number=number,prescription=prescription,pharmacy=pharmacy,status=status,userid=uid,place=place,phone=phone,name=name)
    obj.save()
    return HttpResponse("<script>alert('Uploaded Successfully,The medicine will be cash on delivery');window.location.href='/prescription/'</script>")
    

def pharmacyviewprescription(request):
    uid=request.session['uid']
    obj=prescriptiontable.objects.filter(pharmacy=uid)
    return render(request,'pharmacyviewprescription.html',{'detail':obj})

def presc_status(request):
    id1=request.GET.get("id")
    status=request.GET.get("status")
   
    print ("id1",id1)
    obj=prescriptiontable.objects.get(id=id1)
    obj.status=status
    obj.save()
    return HttpResponse("Successfully Updated")

#updation
def user_feedback(request):
    return render(request,'user_feedback.html',{})

def addfeedback(request):
    userid=request.session["uid"]
    obj=patient_regis.objects.get(lid=userid)
    name=obj.name
    print ("name",name)
    feedback=request.POST.get("feedback")
    ob1=feedbacktable(feedback=feedback,name=name,lid=userid)
    ob1.save()
    print ("feedback",feedback)
    return HttpResponse('<script>alert("Thanks For Your Feedback");window.location.href="/user_feedback/"</script>')

def viewfeedback(request):
    obj=feedbacktable.objects.all()
    return render(request,'adminviewfeedback.html',{'detail':obj})
