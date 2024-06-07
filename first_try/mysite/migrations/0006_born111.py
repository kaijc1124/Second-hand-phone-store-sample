# Generated by Django 5.0.1 on 2024-03-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0005_alter_phone_product_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="born111",
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
                ("City", models.CharField(max_length=3)),
                ("Sum", models.PositiveIntegerField()),
                ("Male", models.PositiveIntegerField()),
                ("Female", models.PositiveIntegerField()),
            ],
        ),
    ]
