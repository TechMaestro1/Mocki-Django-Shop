# Generated by Django 3.2 on 2022-03-07 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0016_alter_comment_imageprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likePost', to='Blog.post'),
        ),
    ]
