# Generated by Django 3.0.2 on 2020-01-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('promocode', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
