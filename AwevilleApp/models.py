from django.db import models
from datetime import datetime
from uuid import uuid4

# Create your models here.
class Message(models.Model):
    """
    A class based model for storing messages submitted from the contact page
    (contact.html)
    """

    Name = models.CharField(max_length=200, default="Anonymous")
    Email = models.CharField(max_length=50, null=False, blank=False)
    Subject = models.CharField(max_length=500, null=False, blank=False)
    Message = models.TextField(blank=False, null=False)

    def __str__(self):
        """
        A string representation of the Message class
        """

        return self.Name
    

class Subscriber(models.Model):
    """
    A class based model for storing subscribers email adresses
    """

    Email = models.CharField(max_length=300)


    def __str__(self):
        """
        A string representation of the Subscriber model
        """

        return self.Email
    

class Booking(models.Model):
    """
    A class based model for keeping customer's booking record
    """
    uniqueID = models.UUIDField( default=uuid4, editable=False)
    Name = models.CharField(max_length=200, default="Anonymous")
    RoomTitle = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=200, blank=False)
    CheckIn = models.CharField(max_length=50, default=datetime.now())
    CheckOut = models.CharField(max_length=50, null=False)
    DateSubmitted = models.DateTimeField(default=datetime.now(), editable=False)
    SpecialRequest = models.TextField(null=True, blank=True)  

    def __str__(self):
        """
        A string representation for the Booking class based model
        """
        return self.Name
    

class Room(models.Model):
    """
    A class based model for keeping room records
    """

    Title = models.CharField(max_length=200)
    Price = models.CharField(max_length=30)
    Description = models.TextField()
    Star = models.IntegerField()
    Image = models.ImageField(upload_to="upload")
    DatePub = models.DateTimeField(default=datetime.now(), editable=False)


    def __str__(self):
        """
        A string representation of the Room class based model
        """

        return self.Title