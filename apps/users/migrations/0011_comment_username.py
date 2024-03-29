# Generated by Django 4.1.6 on 2023-03-24 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_rename_product_comment_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="username",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
