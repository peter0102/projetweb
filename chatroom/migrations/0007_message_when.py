# Generated by Django 4.1 on 2023-01-13 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0006_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="when",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
