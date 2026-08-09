from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "login/",
        LoginView.as_view(template_name="login.html"),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    
    path(
        "contact/",
        views.contact_view,
        name="contact",
    ),
    path("projects/", views.project_list, name="projects"),
    path("register/", views.register_view, name="register"),
    path("contact/", views.contact_view, name="contact"),
    path("skills/", views.skill_list, name="skill_list"),
    path("blog/", views.PostListView.as_view(), name="post_list"),
    path("blog/new/", views.PostCreateView.as_view(), name="post_create"),
    path("blog/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("blog/<slug:slug>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("blog/<slug:slug>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]