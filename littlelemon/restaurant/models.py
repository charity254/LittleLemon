from django.db import models

# Booking table
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) 
    no_of_guests = models.IntegerField()  
    booking_date = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Booking Record - {self.name}, Guests: {self.no_of_guests}, Date: {self.booking_date}"

# Menu table
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField()

    def __str__(self):
        return f"Menu Record - {self.title}, Price: {self.price}, Inventory: {self.inventory}"
