# Generated by Django 4.2.1 on 2023-06-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tartips', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ammo',
        ),
        migrations.DeleteModel(
            name='Calibre',
        ),
    ]
