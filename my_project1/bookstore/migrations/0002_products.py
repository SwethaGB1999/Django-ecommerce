# Generated by Django 5.0 on 2024-01-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=220, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]