# Generated by Django 3.0.1 on 2020-01-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200125_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfotable',
            name='password',
            field=models.CharField(default='1981AA', max_length=5),
        ),
    ]