from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index

from visitor.views import (
    register_visitor, information_visitor, finalize_visit
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name = "login.html",
        ),
        name = "login" 
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name = "logout.html",
        ),
        name = "logout" 
    ),


    path(
        "", 
        index,
        name="index",

    ),

    path(
        "register-visitor/",
        register_visitor,
        name="register-visitor",

    ),

    path(
        "visitors/<int:id>/",
        information_visitor,
        name="information_visitor",

    ),

    path(
        "visitors/<int:id>/finalize-visit/",
        finalize_visit,
        name="finalize_visit",
    )


]

