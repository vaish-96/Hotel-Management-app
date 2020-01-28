from django.db import models

# Create your models here.
class GuestDetails(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    noofdays = models.IntegerField()
    choose_type = models.SmallIntegerField(default=1,blank = False)
    payment_method = models.SmallIntegerField(default=1,blank = False)

    def __str__(self):
        return self.name
    