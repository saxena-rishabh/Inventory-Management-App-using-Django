# Generated by Django 4.1.7 on 2023-03-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0004_alter_item_supplier_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='acquired_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
