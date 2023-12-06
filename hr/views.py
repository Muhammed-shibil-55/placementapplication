from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from myapp.models import Category


from hr.forms import LoginForm,CategoryForm,JobForm
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
                return redirect("index")
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
    template_name="job.html"
    form_class=JobForm
    success_url=reverse_lazy("job")
    

    


    
