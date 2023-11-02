from django.db import models


class ApiRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class DifferenceRequest(ApiRequest):
    number = models.IntegerField(null=False)
    difference = models.IntegerField()
