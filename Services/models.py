from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    service = models.CharField(max_length = 70)
    message = models.CharField(max_length = 500)


    def __str__(self):
        return self.name


class Complaint(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 70)
    message = models.CharField(max_length = 500)


    def __str__(self):
        return self.name


class BookService(models.Model):
    items_json = models.CharField(max_length=2000)
    date = models.DateField()
    time = models.TimeField()
    car = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    licenseno = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name
