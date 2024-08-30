from django.shortcuts import render,redirect
from  django.views.generic import View 
from myapp.models import Cakes
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages








class CakesForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "shape":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","row":5}),
            "pic":forms.FileInput(attrs={"class":"form-control"}),


        }


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

                  

    
class CakesCreativeView(View):
    def get(self,request,*args,**kwrags):
        form=CakesForm()
        return render(request,"cakes-add.html",{"form":form})

    
    def post(self,request,*args,**kwrags):
        form=CakesForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"cakes has been created successfully")
            
            return redirect("cakes-list")
        messages.error(request,"faild to remove")

        return render(request,"cakes-add.html",{"form":form})
    

class CakesListView(View):
    def get(self,request,*args,**kwrags):
        qs=Cakes.objects.all()
        messages.success(request,"cakes has been listed successfully")
        return render(request,"cakes-list.html",{"cakes":qs})
    


class CakesDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cakes.objects.get(id=id)
        messages.success(request,"cakes has been detailed successfully")
        return render(request,"cakes-detail.html",{"cakes":qs})
    


    


class CakesEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        t=Cakes.objects.get(id=id)
        form=CakesForm(instance=t)
       
        return render(request,"cakes-edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        t=Cakes.objects.get(id=id)

        form=CakesForm(instance=t,data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"cakes has been edited successfully")
            
            return redirect("cakes-detail",pk=id)
        
        
        return render(request,"cakes-edit.html",{"form":form})
    


class CakesDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Cakes.objects.get(id=id).delete()
        messages.success(request,"cakes has been removed")
        return redirect("cakes-list")


    


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,"register.html",{"form":form})
    

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            print(usr)
            if usr:
                login(request,usr)
            return redirect("cakes-list")
        return render(request,"login.html",{"form":form})
    

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

        



    

    

             
             

    
    
