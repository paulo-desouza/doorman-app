from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class BasicUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email =  self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False 

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario
    

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True 

        usuario.set_password(password)
        usuario.save()
        return usuario
    


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
    
