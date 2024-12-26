from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    title = models.CharField(max_length=20)
    note = models.TextField()  # Field for storing the note
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # FK to the User model

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the note is created
