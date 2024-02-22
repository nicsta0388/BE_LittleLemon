from django.db import models
from PIL import Image
from datetime import datetime

# Create your models here.
# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     reservation_date = models.DateField()
#     reservation_slot = models.SmallIntegerField(default=10)

#     def __str__(self): 
#         return self.first_name

# class Menu(models.Model):
#    name = models.CharField(max_length=200) 
#    price = models.IntegerField(null=False) 
#    menu_item_description = models.TextField(max_length=1000, default='') 

#    def __str__(self):
#         return self.name
    
# Create your models here.
class Menu(models.Model):
    #id = models.IntegerField(primary_key=True,)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(null="True")
    description = models.CharField(max_length=500)
    image = models.ImageField(default='./static/img/salad.jpg', upload_to='menu-images/', null="True")

    def __str__(self):
        return f'{self.title} : {str(self.price)} , {str(self.description)}'

class Booking(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField( default=1)
    BookingDate = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=255, default='little@lemon.com')
    phone_number = models.IntegerField( default=0)

    def __str__(self):
        return f'{self.name} : {self.no_of_guests}'

    # def __str__(self) -> str:
    #     return f'{self.name} : {self.no_of_guests}'

class Employees(models.Model):
    name = models.CharField(max_length= 200)
    department = models.CharField(max_length= 200)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(null="True")

    def __str__(self):
        return f'{self.title} : {str(self.price)}'