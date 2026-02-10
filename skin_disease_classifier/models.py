from django.db import models


class SkinImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Prediction(models.Model):
    image = models.ForeignKey(SkinImage, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=200)
    confidence = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    action = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

