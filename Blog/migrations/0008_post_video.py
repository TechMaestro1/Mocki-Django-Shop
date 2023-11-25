# Generated by Django 3.2 on 2022-03-02 05:56

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_remove_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=Blog.models.upload_src_video),
        ),
    ]