# Generated by Django 5.1 on 2024-08-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_student_file_alter_student_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
        migrations.RemoveField(
            model_name="student",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.TextField(),
        ),
    ]
