# Generated by Django 3.0.1 on 2020-02-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200125_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfotable',
            name='password',
            field=models.CharField(default='B3TGE', max_length=5),
        ),
    ]