# Generated by Django 4.1.3 on 2022-11-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('value', models.CharField(max_length=1000000000)),
                ('user', models.CharField(max_length=20000000000)),
                ('room', models.CharField(max_length=200000000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
            ],
        ),
    ]