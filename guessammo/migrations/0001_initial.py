# Generated by Django 4.2.1 on 2023-06-02 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ammo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
                ('calibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guessammo.calibre')),
            ],
        ),
    ]
