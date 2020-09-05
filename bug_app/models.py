from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class MyUser(AbstractUser):
    bio = models.CharField(max_length=150, blank=True, unique=True)
    REQUIRED_FIELDS = ['bio']

    def __str__(self):
        return f"{self.username}"


class Ticket(models.Model):
    STATUS_CHOICES = (
        ("NEW", "NEW"),
        ("IN_PROGRESS", "IN_PROGRESS"),
        ("DONE", "DONE"),
        ("INVALID", "INVALID")
    )

    title = models.CharField(max_length=50)
    post_date = models.DateTimeField(
        default=timezone.now)
    description = models.TextField()
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default="NEW")

    filed = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    assigned = models.ForeignKey(
        MyUser, related_name="assigned_user", on_delete=models.CASCADE, null=True)
    completed = models.OneToOneField(
        MyUser, related_name="completed_user", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
