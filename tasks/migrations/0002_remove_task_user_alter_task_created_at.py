# Generated by Django 5.1.1 on 2024-10-02 10:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="user",
        ),
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
