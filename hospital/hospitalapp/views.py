from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PatientModel, DoctorModel,PharmacyModel,LabModel
import joblib

# Create your views here.
def mainhomepage(request):
    return render(request,"mainhomepage.html",)

def homepage(request):
    return render(request,"homepage.html",)
def loginuser(request):
    return render(request,"userlogin.html")
def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None:
        login(request, user)
        return redirect('homepage')
    # if user doesn't exists
    if user is None:
        messages.add_message(request, messages.ERROR, "Wrong password. Try again ")
        return redirect('userlogin')
def signupuser(request):
    username =request.POST['username']
    password =request.POST['password']
    phoneno =request.POST['phoneno']

# If username already exists
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"user already exists")
        return redirect('/#/')
# If username exists
    User.objects.create_user(username=username,password= password).save()
    lastobject = len(User.objects.all())-1
    PatientModel(userid = User.objects.all()[int(lastobject)].id, phoneno = phoneno).save()
    messages.add_message(request, messages.ERROR, "user successfully created")
    return  redirect('userlogin')

def doctormodel(request):
    context = {'doctor':DoctorModel.objects.all(),'length':0}
    return render(request,"Doctorconsult.html",context)

def pharmacymodel(request):
    context = {'medicine':PharmacyModel.objects.all()}
    return render(request,"pharmacy.html",context)

def labmodel(request):
    context = {'labtest':LabModel.objects.all()}
    return render(request,"lab.html",context)

def logout(request):
    request.session.clear()
    return redirect("/#/")
def prediction(request):
    # o2 =[[-0.06559225 ,-1.2897233 , -0.28528602 ,-0.75725254, -0.78992993 ,-0.51777378 ,-0.62093975 ,-0.91332148 ,-0.86268515,-0.90641175,0.16788041,-0.69367014]]
    return render(request, "prediction.html")

def result(request):
    # o2 = [1.97259859e-01 ,1.71303831e-01 ,1.96489473e-01,-5.80766382e-01,-8.12834215e-01,-5.04178488e-01 ,2.22907687e-01,-4.79828115e-05,-4.29392231e-01,-7.31145526e-01,-7.78476227e-01,-5.98401236e-01]

    pre = joblib.load("finalized_model.sav")
    lis=[]
    lis.append(request.GET['radius_mean'])
    lis.append(request.GET['texture_mean'])
    lis.append(request.GET['smoothness_mean'])
    lis.append(request.GET['compactness_mean'])
    lis.append(request.GET['symmetry_mean'])
    lis.append(request.GET['fractal_dimension_mean'])
    lis.append(request.GET['radius_se'])
    lis.append(request.GET['texture_se'])
    lis.append(request.GET['smoothness_se'])
    lis.append(request.GET['compactness_se'])
    lis.append(request.GET['symmetry_se'])
    lis.append(request.GET['fractal_dimension_se'])
    ans = pre.predict([lis])
    return render(request, 'result.html', {'ans': ans})
