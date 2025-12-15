from django.db import models
from django.contrib.auth.models import User

class Smoothie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="smoothies"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
