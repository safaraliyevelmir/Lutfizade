# Generated by Django 3.2.5 on 2021-07-25 15:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Başlıq')),
                ('image', models.ImageField(upload_to='blog')),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
