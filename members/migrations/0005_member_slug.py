# Generated by Django 5.0 on 2023-12-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_rename_members_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]