# Generated by Django 5.0 on 2023-12-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_menu_items_purchase_purchase_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
