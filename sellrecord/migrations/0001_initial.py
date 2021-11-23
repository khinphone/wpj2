# Generated by Django 3.2.9 on 2021-11-20 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=11)),
                ('purchase_items', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('showroom', models.CharField(max_length=255)),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
    ]
