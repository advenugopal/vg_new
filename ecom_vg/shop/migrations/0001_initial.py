# Generated by Django 4.2.15 on 2024-09-30 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField()),
                ("image", models.ImageField(upload_to="category")),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField()),
                ("image", models.ImageField(upload_to="product")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("available", models.BooleanField(default=True)),
                ("stock", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.category"
                    ),
                ),
            ],
        ),
    ]