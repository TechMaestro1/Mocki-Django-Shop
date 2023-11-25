# Generated by Django 3.2 on 2022-02-24 18:55

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('coverImage', models.ImageField(upload_to=Blog.models.upload_src_cover_image)),
            ],
        ),
    ]