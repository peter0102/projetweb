# Generated by Django 4.1 on 2023-01-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("roomName", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="Account",
        ),
    ]
