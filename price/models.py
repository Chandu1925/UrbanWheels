from django.db import models

class Rental(models.Model):
    cust_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)  # Assuming you want to include the email field
    bike_name = models.CharField(max_length=100,null=True)
    rental_type = models.CharField(max_length=20,choices=[('hourly', 'Per Hour'), ('daily', 'Per Day'), ('monthly', 'Per Month')])
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.cust_name} - {self.bike_name} ({self.rental_type})"
