# Generated by Django 4.1 on 2023-01-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0004_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]