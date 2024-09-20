from django.db import models

class Sanction(models.Model):
    title = models.CharField(max_length=100, null=True)
    pdf = models.FileField(upload_to='pdf/', null=True)

    def __str__(self):
        return self.title[:20]