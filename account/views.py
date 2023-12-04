from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product



# Create your views here.

# class RegView(View):
#     form_class=RegForm
#     template_name="reg.html"
#     model=User
#     success_url="log"

#     def get(self,request):
#         form=self.form_class()
#         context={}
#         context["form"]=form
#         return render(request,self.template_name,context)
#     def post(self,request):
#         form_data=self.form_class(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registration successfull!!")
#             return redirect(self.success_url)
#         return render(request,self.template_name,{"form":form_data})


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('log')
    def form_valid(self, form):
        messages.success(self.request,"Registration successful !!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Validation failed")
        return super().form_invalid(form)

# class LogView(View):
#     def get(self,request):
#         form=LogForm()
#         return render(request,'log.html',{"form":form})
#     def post(self,request):
#         form_data=LogForm(data=request.POST)
#         if form_data.is_valid():
#             uname=form_data.cleaned_data.get("user_name")
#             pswd=form_data.cleaned_data.get("password")
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 messages.success(request,"login successfull !!")
#                 login(request,user)
#                 return redirect('home')
#             else:
#                 messages.success(request,"Invalid username or password !!")
#                 return redirect('log')
#         return render(request,"log.html",{"form":form_data})



class LogView(FormView):
    template_name='log.html'
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("user_name")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                messages.success(request,"login successfull !!")
                login(request,user)
                return redirect('home')
            else:
                messages.success(request,"Invalid username or password !!")
                return redirect('log')
        return render(request,"log.html",{"form":form_data})
            
        
            
# class HomeView(TemplateView):
#     template_name="home.html"

class HomeView(ListView):
    template_name="home.html"
    queryset=Product.objects.all()
    context_object_name="data"

class LgOutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')