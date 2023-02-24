# Generated by Django 4.1.3 on 2022-11-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0006_cart_cartitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("client_name", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("district", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=1000)),
                ("pincode", models.IntegerField()),
                ("phone1", models.IntegerField()),
                ("phone2", models.IntegerField()),
                ("email", models.CharField(max_length=100)),
            ],
        ),
    ]