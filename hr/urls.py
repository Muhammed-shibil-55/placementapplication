from django.urls import path
from hr import views



urlpatterns=[
        path("signin/",views.SignInView.as_view(),name="signin"),
        path("signout/",views.SignOutView.as_view(),name="signout"),
        path("index/",views.DashBoardView.as_view(),name="index"),
        path("category/add/",views.CategoryCreateListView.as_view(),name="category"),
        path("category/<int:pk>/remove",views.CategoryDeleteView.as_view(),name="category-delete"),
        path("job/",views.JobCreateView.as_view(),name="job"),
]