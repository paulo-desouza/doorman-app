from django.db import models

class Doorman(models.Model):

    basic_user = models.OneToOneField(
        "basic_user.BasicUser",
        verbose_name = "User",
        on_delete = models.PROTECT

    )

    full_name = models.CharField(
        verbose_name = "Full Name",
        max_length = 194,

    )

    SSN = models.CharField(
        verbose_name = "SSN",
        max_length = 9,

    )

    phone_number = models.CharField(
        verbose_name = "Contact Phone Number",
        max_length = 11,

    )

    birth_date = models.DateField(
        verbose_name = "Birth Date",
        auto_now=False,
        auto_now_add=False,

    )

    class Meta:
        verbose_name = "Doorman"
        verbose_name_plural = "Doormen"
        db_table = "doorman"

    def __str__(self):
        return self.full_name
    


