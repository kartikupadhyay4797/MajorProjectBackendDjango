# Generated by Django 3.0.1 on 2020-02-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0011_auto_20200128_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerinfotable',
            name='password',
            field=models.CharField(default='YMVNG', max_length=5),
        ),
    ]