from django.db import models



# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('user', 'USER'),
    ]
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices= ROLE_CHOICES, null=True)



class BikeBooking(models.Model):
    BIKE_MODELS = [
        ('PANIGALE V4', 'PANIGALE V4'),
        ('ROADSTER SS', 'ROADSTER SS'),
        ('S1000RR', 'S1000RR'),
        ('STREET TRIPLE', 'STREET TRIPLE'),
        ('FIREBLADE RR', 'FIREBLADE RR'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bike_model = models.CharField(max_length=50, choices=BIKE_MODELS)
    booking_date = models.DateField()
    rental_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=200,decimal_places=2)



    def __str__(self):
        return f"{self.name} - {self.bike_model} ({self.booking_date})"




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
