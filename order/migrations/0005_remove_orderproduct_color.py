# Generated by Django 4.2.7 on 2023-11-19 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderproduct_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
    ]
