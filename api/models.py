from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title[:10]
