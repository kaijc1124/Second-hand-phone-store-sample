# Generated by Django 5.0.1 on 2024-04-06 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_alter_phone_product_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="phone_product", old_name="owner", new_name="Owner",
        ),
    ]
