# Generated by Django 4.1.7 on 2023-03-29 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=20)),
                ('brandName', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('supplier', models.CharField(max_length=20)),
                ('supplier_contact_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('acquired_date', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('expiry_date', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
            ],
        ),
    ]
