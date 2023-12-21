from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
# Create your views here.
from jobseeker.forms import SignupForm,Profileform
from django.urls import reverse_lazy
from myapp.models import StudentProfile,Jobs,Applications


class SignUpView(CreateView):
    template_name="jobseeker/register.html"
    form_class=SignupForm
    success_url=reverse_lazy("signin")


class StudentIndexView(ListView):
    template_name="jobseeker/index.html"
    context_object_name="data"
    model=Jobs

    def get_queryset(self):
        my_applications=Applications.objects.filter(student=self.request.user).values_list("job",flat=True)
        qs=Jobs.objects.exclude(id__in=my_applications).order_by("-created_date")
        return qs

class ProfileCreateView(CreateView):
    template_name="jobseeker/profile_add.html"
    form_class=Profileform
    success_url=reverse_lazy("seeker-index")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class ProfileDetailView(DetailView):
    template_name="jobseeker/profile_detail.html"
    context_object_name="data"
    model=StudentProfile

class ProfileUpdateView(UpdateView):
    template_name="jobseeker/profile_edit.html"
    form_class=Profileform
    model=StudentProfile
    success_url=reverse_lazy("seeker-index")

# class JobListView(ListView):
#     template_name="jobseeker/job_list.html"
#     model=Jobs
#     context_object_name="jobs"


class JobDetailView(DetailView):
    template_name="jobseeker/job-detail.html"
    model=Jobs
    context_object_name="data"

class JobApplyView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_object=Jobs.objects.get(id=id)
        user_object=request.user
        Applications.objects.create(job=job_object,student=user_object)
        return redirect("seeker-index")
    

class ApplicationListView(ListView):
    template_name="jobseeker/applications.html"
    model=Applications
    context_object_name="data"

    def get_queryset(self):
        qs=Applications.objects.filter(student=self.request.user)
        return qs

class JobSaveView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_object=Jobs.objects.get(id=id)
        action=request.POST.get("action")
        if action=="save":
            request.user.profile.saved_jobs.add(job_object)
        elif action=="unsave":
            request.user.profile.saved_jobs.remove(job_object)
        return redirect("seeker-index")
    

class SavedJobsView(View):
    def get(self,request,*ars,**kwargs):
        qs=request.user.profile.saved_jobs.all()
        return render(request,"jobseeker/saved-jobs.html",{"data":qs})