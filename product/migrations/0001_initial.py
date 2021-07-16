# Generated by Django 3.2.5 on 2021-07-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('explanation', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
