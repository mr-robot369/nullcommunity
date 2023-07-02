from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.IndexPage, name="index"),
    path("upload/",views.UploadData, name="infoupload"),
    path("profile/",views.ProfileFetch, name="show"),
    path("editprofile/<int:pk>", views.EditProfile, name="edit"),
    path("update/<int:pk>", views.UpdateData, name="update"),
]