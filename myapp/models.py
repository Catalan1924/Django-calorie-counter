from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    name     = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date     = models.DateField(default=timezone.localdate)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"