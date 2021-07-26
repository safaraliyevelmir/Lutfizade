from django.db import models

class Idea(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
