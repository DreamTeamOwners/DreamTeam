# Generated by Django 4.1.6 on 2023-03-24 08:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="username",
        ),
    ]