# Generated by Django 3.1.7 on 2021-05-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_orders_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='approveds_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('approved', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]