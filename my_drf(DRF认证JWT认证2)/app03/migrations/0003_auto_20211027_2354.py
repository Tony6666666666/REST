# Generated by Django 3.1.5 on 2021-10-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
