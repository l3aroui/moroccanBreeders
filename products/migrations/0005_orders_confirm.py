# Generated by Django 4.2.1 on 2023-06-18 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_cart_date_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_Confirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.itempanier')),
            ],
        ),
    ]
