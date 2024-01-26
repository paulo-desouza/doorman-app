from django.db import models

class Visitor(models.Model):

    STATUS_VISITOR = [
        ("AWAITING", "Awaiting Authorization"),
        ("IN_VISIT", "In Visit"),
        ("FINALIZED", "Visit has been finalized"),
    ]

    status = models.CharField(
        verbose_name = "Status",
        max_length = 10,
        choices = STATUS_VISITOR,
        default = "AWAITING"
    )


    full_name = models.CharField(
        verbose_name = "Full Name",
        max_length = 194,

    )

    ssn = models.CharField(
        verbose_name = "SSN",
        max_length = 9,

    )

    birth_date = models.DateField(
        verbose_name = "Birth Date",
        auto_now_add = False,
        auto_now = False,

    )

    apartment_number = models.PositiveSmallIntegerField(
        verbose_name = "Apartment Number to be visited",

    )

    vehicle_plate = models.CharField(
        verbose_name = "Vehicle Plate Number",
        max_length = 7,
        blank = True,
        null = True,
    )

    arrival_time = models.DateTimeField(
        verbose_name = "Arrival Time of Guest",
        auto_now_add = True,

    )

    checkout_time = models.DateTimeField(
        verbose_name = "Guest Checkout Time",
        auto_now = False,
        blank = True,
        null = True,

    )

    authorization_time = models.DateTimeField(
        verbose_name = "Time of Entry Authorization",
        auto_now = False,
        blank = True,
        null = True,

    )

    responsible_tenant = models.CharField(
        verbose_name = "Name of Tenant responsible for the guest's visit",
        max_length = 194,
        blank = True, 

    )

    registered_by = models.ForeignKey(
        "doorman.Doorman",
        verbose_name = "Doorman responsible for registering this guest",
        on_delete = models.PROTECT,

    )




    def get_checkout_time(self):
        if self.checkout_time:
            return self.checkout_time
        
        return "Checkout Time not registered"
    
    def get_authorization_time(self):
        if self.authorization_time:
            return self.authorization_time
        
        return "Guest Awaiting Authorization"
    
    def get_responsible_tenant(self):
        if self.responsible_tenant:
            return self.responsible_tenant
        
        return "Guest Awaiting Authorization"
    
    def get_vehicle_plate(self):
        if self.vehicle_plate:
            return self.vehicle_plate
        
        return "Vehicle Plate not registered."
    
    def get_ssn(self):
        if self.ssn:
            ssn = str(self.ssn)

        ssn_1 = ssn[0:3]
        ssn_2 = ssn[3:5]
        ssn_3 = ssn[5:]

        ssn_formatted = f"{ssn_1}-{ssn_2}-{ssn_3}"

        return ssn_formatted
    
    


    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"
        db_table = "visitor"

    def __str__(self):
        return self.full_name
    

    