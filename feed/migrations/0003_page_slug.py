# Generated by Django 4.1.7 on 2023-02-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
