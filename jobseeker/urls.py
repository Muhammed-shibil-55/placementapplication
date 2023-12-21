from django.urls import path

from jobseeker import views

urlpatterns = [
       path("register/",views.SignUpView.as_view(),name="signup"),
       path("index/",views.StudentIndexView.as_view(),name="seeker-index"),
       path("profile/add/",views.ProfileCreateView.as_view(),name="profile-add"),
       path("profile/<int:pk>/",views.ProfileDetailView.as_view(),name="profile-detail"),
       path("profile/<int:pk>/change",views.ProfileUpdateView.as_view(),name="profile-edit"),
       path("job/<int:pk>/detail/",views.JobDetailView.as_view(),name="job-detail"),
       path("job/<int:pk>/apply/",views.JobApplyView.as_view(),name="job-apply"),
       path("applications/all/",views.ApplicationListView.as_view(),name="myapplications"),
       path("jobs/<int:pk>/save/",views.JobSaveView.as_view(),name="job-save"),
       path("profile/job/saved/",views.SavedJobsView.as_view(),name="saved-jobs"),
]