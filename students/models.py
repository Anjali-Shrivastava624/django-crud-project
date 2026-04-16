from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name    = models.CharField(max_length=100)
    email   = models.EmailField(unique=True)
    age     = models.PositiveIntegerField()
    course  = models.CharField(max_length=100)
    gender  = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone   = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name