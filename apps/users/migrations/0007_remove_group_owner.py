# Generated by Django 4.1.6 on 2023-03-24 03:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_group_owner_alter_group_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="owner",
        ),
    ]
