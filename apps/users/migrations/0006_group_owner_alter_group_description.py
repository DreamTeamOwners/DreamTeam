# Generated by Django 4.1.6 on 2023-03-24 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_group_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner_group",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="group",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
