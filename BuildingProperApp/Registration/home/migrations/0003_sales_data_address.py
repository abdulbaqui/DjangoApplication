# Generated by Django 3.0.6 on 2020-06-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200605_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_data',
            name='Address',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]