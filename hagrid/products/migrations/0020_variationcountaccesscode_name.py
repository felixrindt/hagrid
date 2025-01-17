# Generated by Django 5.1.4 on 2024-12-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_variation_count_disabled_reason_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="variationcountaccesscode",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="A name to identify or describe this code to admins (only shown there)",
                max_length=32,
                null=True,
            ),
        ),
    ]
