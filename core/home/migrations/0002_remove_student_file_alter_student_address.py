# Generated by Django 5.1 on 2024-08-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="file",
        ),
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.TextField(blank=True),
        ),
    ]