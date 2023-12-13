from django.shortcuts import render
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView
# Create your views here.
from jobseeker.forms import SignupForm,Profileform
from django.urls import reverse_lazy
from myapp.models import StudentProfile


class SignUpView(CreateView):
    template_name="jobseeker/register.html"
    form_class=SignupForm
    success_url=reverse_lazy("signin")


class StudentIndexView(TemplateView):
    template_name="jobseeker/index.html"

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