# Generated by Django 3.0.1 on 2020-01-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200125_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfotable',
            name='password',
            field=models.CharField(default='XG98J', max_length=5),
        ),
    ]
