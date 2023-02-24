# Generated by Django 4.1.3 on 2022-11-16 07:30

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_ad_product_ppoi"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="product_image",
        ),
        migrations.AddField(
            model_name="product",
            name="maintenance",
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="product_image1",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                null=True,
                upload_to="image/testimagemodel/",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_image2",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                null=True,
                upload_to="image/testimagemodel/",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_image3",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                null=True,
                upload_to="image/testimagemodel/",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_image4",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                null=True,
                upload_to="image/testimagemodel/",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="specifications",
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]