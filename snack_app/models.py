from django.db import models

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Flavor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    snack = models.ForeignKey(Snack, related_name="flavors", on_delete=models.CASCADE)