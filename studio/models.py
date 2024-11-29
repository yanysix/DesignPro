from django.db import models
from django.contrib.auth.models import User

class DesignRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    room_size = models.CharField(max_length=50)
    description = models.TextField()
    style_preferences = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.user.username} for {self.room_type}"