# Generated by Django 4.1 on 2023-01-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0003_delete_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("message", models.CharField(max_length=10000)),
                ("where", models.CharField(max_length=1000)),
            ],
        ),
    ]
