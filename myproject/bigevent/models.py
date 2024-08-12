from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class People(models.Model):
    fullname = models.CharField(max_length=45, null=False, unique=True)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, null=False, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.fullname  # String representation of the model


class Event(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ticket_number = models.IntegerField(default=1, null=False, unique=True)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)

    def __str__(self):
        return f"Event {self.ticket_number} on {self.date}"  # String representation of the model


class Attendance(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)  # Foreign key to People
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Foreign key to Event

    def __str__(self):
        return f"{self.person.fullname} at Event {self.event.ticket_number}"
