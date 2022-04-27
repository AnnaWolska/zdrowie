from django.db import models
from django.contrib.auth.models import User


class Bloodpressure(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="bloodpressures")
    date = models.DateTimeField(auto_now_add=True)
    result1 = models.IntegerField(null=True, blank=True)
    result2 = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} ({self.date} {self.result1} {self.result2} {self.comment})"

    class Meta:
        verbose_name = "ciśnienie"
        verbose_name_plural = "ciśnienia"


class Glucoses(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="bloodpressures")
    date = models.DateTimeField(auto_now_add=True)
    result1 = models.IntegerField(null=True, blank=True)
    # result2 = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} ({self.date} {self.result1} {self.comment})"

    class Meta:
        verbose_name = "pomiar cukru"
        verbose_name_plural = "pomiary cukru"