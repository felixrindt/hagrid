# Generated by Django 4.2.16 on 2024-12-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_variation_count_disabled_reason_and_more"),
        ("gallery", "0004_galleryimage_alt_text_alter_galleryimage_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="galleryimage",
            name="variation",
        ),
        migrations.AddField(
            model_name="galleryimage",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="galleryimage",
            name="sizegroup",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.sizegroup",
            ),
        ),
    ]
