# Generated by Django 3.0.6 on 2020-06-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200608_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
