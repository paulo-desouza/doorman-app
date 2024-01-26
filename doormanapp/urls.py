from django.contrib import admin
from django.urls import path

from basic_user.views import index
from visitor.views import (
    register_visitor, information_visitor
)


urlpatterns = [
    path("admin/", admin.site.urls),
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

    )
]

