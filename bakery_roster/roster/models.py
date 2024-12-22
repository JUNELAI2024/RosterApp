from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Roster(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # e.g., "Sun", "Mon"
    timeslot = models.CharField(max_length=10)  # e.g., "A.M.", "P.M."

    def __str__(self):
        return f"{self.staff.name} - {self.day}: {self.timeslot}"