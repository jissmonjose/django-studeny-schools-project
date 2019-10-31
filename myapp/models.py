from django.db import models
from django.shortcuts import reverse


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:school_details', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:student_details', kwargs={'pk': self.pk})
