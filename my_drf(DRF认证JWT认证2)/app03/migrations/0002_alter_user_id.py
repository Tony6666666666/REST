# Generated by Django 3.2.8 on 2021-10-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
