# Generated by Django 3.0.1 on 2020-02-16 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0012_auto_20200216_1401'),
        ('dealer', '0012_auto_20200216_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderCreatedDate', models.DateTimeField(auto_now=True)),
                ('orderItems', models.CharField(max_length=200)),
                ('orderItemsQuantity', models.CharField(max_length=50)),
                ('orderItemsPrice', models.CharField(max_length=200)),
                ('orderItemsTotalPrice', models.CharField(max_length=200)),
                ('orderTotalPrice', models.CharField(max_length=10)),
                ('orderStatus', models.CharField(max_length=50)),
                ('orderReviewText', models.CharField(max_length=200)),
                ('orderReviewStarRating', models.CharField(max_length=1)),
                ('orderWithPromocode', models.CharField(max_length=100)),
                ('orderPaymentMethod', models.CharField(max_length=100)),
                ('orderPaymentStatus', models.CharField(max_length=100)),
                ('orderByUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userInfoTable')),
                ('orderToDealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealerInfoTable')),
            ],
        ),
    ]