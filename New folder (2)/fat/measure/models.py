from django.db import models

# Create your models here.
class BodyFatPrediction(models.Model):
    density = models.FloatField()
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    neck = models.FloatField()
    chest = models.FloatField()
    abdomen = models.FloatField()
    hip = models.FloatField()
    thigh = models.FloatField()
    knee = models.FloatField()
    ankle = models.FloatField()
    biceps = models.FloatField()
    forearm = models.FloatField()
    wrist = models.FloatField()
    predicted_bodyfat = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"BodyFatPrediction: {self.pk}"