from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import random
import string


class CustomUser(AbstractUser):
    is_villager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Custom related_name to avoid clashes
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Custom related_name to avoid clashes
        blank=True
    )




def generate_complaint_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Complaint(models.Model):
    DEPARTMENT_CHOICES = [
        ('health', 'Health'),
        ('transport', 'Transport'),
        ('agriculture', 'Agriculture'),
        ('water', 'Water'),
        ('education', 'Education'),
        ('electricity', 'Electricity'),
        ('other', 'Other'),
    ]

class Complaint(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255, default='Default Location')  # Set the default value here
    department = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    complaint = models.TextField()
    complaint_id = models.CharField(max_length=20, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when a complaint is created
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('solved', 'Solved'),
    ], default='pending')
    def __str__(self):
        return self.complaint_id
