from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/<str:username>/", views.profile, name="profile"),
    path("detail/<str:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("edit/<str:pk>/", views.edit, name="edit"),
    path("update/<str:pk>/", views.update, name="update"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("userDelete/", views.userDelete, name="userDelete"),
]
