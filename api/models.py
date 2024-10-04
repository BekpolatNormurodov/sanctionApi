from datetime import date
from django.db import models

# Oper
class SanctionOper(models.Model):
    date = models.DateField(default=date.today)
    hackType = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    shakl1 = models.CharField(max_length=10, null=True)
    pdf = models.FileField(upload_to='pdf/', null=True)

    def __str__(self):
        return self.shakl1[:10]
    


# IIB
class SanctionIIB(models.Model):
    date = models.DateField(default=date.today)
    hackType = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    shakl1 = models.CharField(max_length=10, null=True)
    pdf = models.FileField(upload_to='pdf/iib/', null=True)

    def __str__(self):
        return self.shakl1[:10]
    

# Prokuratura
class SanctionProkuratura(models.Model):
    date = models.DateField(default=date.today)
    hackType = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    shakl1 = models.CharField(max_length=10, null=True)
    pdf = models.FileField(upload_to='pdf/prokuratura/', null=True)

    def __str__(self):
        return self.shakl1[:10]


# Oper Star
class SanctionStar(models.Model):
    starId = models.IntegerField(null=True)

    def __str__(self):
        return self.starId[:10]