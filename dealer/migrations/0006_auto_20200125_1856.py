# Generated by Django 3.0.1 on 2020-01-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0005_auto_20200125_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerinfotable',
            name='password',
            field=models.CharField(default='MN2VC', max_length=5, unique=True),
        ),
    ]