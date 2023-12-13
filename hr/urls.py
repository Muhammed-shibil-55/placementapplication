from django.urls import path
from hr import views




urlpatterns=[
        path("",views.SignInView.as_view(),name="signin"),
        path("signout/",views.SignOutView.as_view(),name="signout"),
        path("index/",views.DashBoardView.as_view(),name="index"),
        path("category/add/",views.CategoryCreateListView.as_view(),name="category"),
        path("category/<int:pk>/remove",views.CategoryDeleteView.as_view(),name="category-delete"),
        path("job/add/",views.JobCreateView.as_view(),name="job-add"),
        path("jobs/all/",views.JobListView.as_view(),name="job-list"),
        path("job/<int:pk>/remove",views.JobDeleteView.as_view(),name="job-remove"),
        path("job/<int:pk>/change",views.JobUpdateView.as_view(),name="job-change")
]