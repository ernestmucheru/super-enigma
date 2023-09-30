from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Travels(models.Model):
    name = models.CharField(max_length=200, blank=False)
    Location = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(max_length=2000, blank=False)
    image = CloudinaryField('image')

    class Meta:
        verbose_name_plural = "Travels"

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    client_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural = "Bookings"

    def __str__(self):
        return str(self.start_date)
