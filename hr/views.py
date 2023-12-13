from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from myapp.models import Category,Jobs


from hr.forms import LoginForm,CategoryForm,JobForm,JobChangeForm
# Create your views here.


class SignInView(FormView):
    template_name="signin.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                print("session started")
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("seeker-index")
            else:
                print("login failed")
                return render(request,"signin.html",{"form":form})
        print("invalid form")
        return render(request,"signin.html",{"form":form})
    
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        print("session ended")
        return redirect("signin")
    
class DashBoardView(TemplateView):
    template_name="index.html"


class CategoryCreateListView(CreateView,ListView):
    template_name="category.html"
    form_class=CategoryForm
    success_url=reverse_lazy("category")
    context_object_name="data"
    model=Category

   
    

class CategoryDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return redirect("category")
    



class JobCreateView(CreateView):
    template_name="job-add.html"
    form_class=JobForm
    success_url=reverse_lazy("index")

class JobListView(ListView):
    template_name="job-list.html"
    context_object_name="jobs"
    model=Jobs

    def get(self,request,*args,**kwargs):
        qs=Jobs.objects.all()
        if "status" in request.GET:
            value=request.GET.get("status")
            qs=qs.filter(status=value)
        return render(request,self.template_name,{"jobs":qs})
    
    
    # def get_queryset(self):
    #     return Jobs.objects.filter(status=True)

class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Jobs.objects.filter(id=id).delete()
        return redirect("job-list")
    

class JobUpdateView(UpdateView):
    form_class=JobChangeForm
    template_name="job-edit.html"
    model=Jobs
    success_url=reverse_lazy("job-list")
    

    


    
