from django.db import models
from django.db.models.fields import DateField
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField("Başlıq",max_length=256)
    image = models.ImageField(upload_to="blog")
    content = RichTextField()
    date = DateField(auto_now_add=True)


    def __str__(self):
        return self.title