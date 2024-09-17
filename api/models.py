from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='image/')
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title[:10]
