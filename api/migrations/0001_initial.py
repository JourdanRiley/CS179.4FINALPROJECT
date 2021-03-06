# Generated by Django 2.0.4 on 2018-04-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('cart_code', models.CharField(max_length=30)),
                ('total_price', models.FloatField()),
                ('paid', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('product_name', models.TextField()),
                ('product_description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('shipping_address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='Products',
            field=models.ManyToManyField(to='api.Product'),
        ),
    ]
