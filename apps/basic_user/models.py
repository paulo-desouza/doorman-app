from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class BasicUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        basic_user = self.model(
            email =  self.normalize_email(email)
        )

        basic_user.is_active = True
        basic_user.is_staff = False
        basic_user.is_superuser = False 

        if password:
            basic_user.set_password(password)

        basic_user.save()

        return basic_user
    

    def create_superuser(self, email, password):
        basic_user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        basic_user.is_active = True
        basic_user.is_staff = True
        basic_user.is_superuser = True 

        basic_user.set_password(password)
        basic_user.save()
        return basic_user
    


class BasicUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name = "User Email",
        max_length = 194,
        unique=True,
    )


    is_active = models.BooleanField(
        verbose_name = "User is active",
        default =  True,
    )

    is_staff = models.BooleanField(
        verbose_name="User is from development team",
        default=False,
    
    )

    is_superuser = models.BooleanField(
        verbose_name="Usser is a superuser",
        default = False,
    )

    USERNAME_FIELD = "email"
    objects = BasicUserManager()



    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"


    def __str__(self):
        return self.email
    
