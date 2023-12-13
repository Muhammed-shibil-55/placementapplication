from django.urls import path

from jobseeker import views

urlpatterns = [
       path("register/",views.SignUpView.as_view(),name="signup"),
       path("index/",views.StudentIndexView.as_view(),name="seeker-index"),
       path("profile/add/",views.ProfileCreateView.as_view(),name="profile-add"),
       path("profile/<int:pk>/",views.ProfileDetailView.as_view(),name="profile-detail"),
       path("profile/<int:pk>/change",views.ProfileUpdateView.as_view(),name="profile-edit")
]