# Generated by Django 3.0.1 on 2020-01-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200125_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfotable',
            name='password',
            field=models.CharField(default='AFE2F', max_length=5),
        ),
        migrations.AlterField(
            model_name='userinfotable',
            name='refercode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
