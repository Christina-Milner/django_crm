from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    # Not using number because we don't want to do math on that and in some countries, zip codes have letters

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    # Django handles all the DB interaction stuff
    # but need to use migrate again after setting this up
    # python manage.py makemigrations
    # python manage.py migrate