from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    class Meta:

        verbose_name = 'student'
        verbose_name_plural = 'students'

    student_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    student_points = models.FloatField()
    
    def __str__(self):
        return f"{self.student_name}, {self.student_id}"
