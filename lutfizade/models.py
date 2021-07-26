from django.db import models



class Aboutme(models.Model):
    title = models.CharField(max_length=256)
    detail = models.TextField()

    def __str__(self):
        return self.title
