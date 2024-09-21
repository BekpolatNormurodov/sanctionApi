from datetime import date
from django.db import models

class Sanction(models.Model):
    date = models.DateField(default=date.today)
    region = models.CharField(max_length=50, null=True)
    shakl1 = models.CharField(max_length=10, null=True)
    pdf = models.FileField(upload_to='pdf/', null=True)

    def __str__(self):
        return self.shakl1[:10]