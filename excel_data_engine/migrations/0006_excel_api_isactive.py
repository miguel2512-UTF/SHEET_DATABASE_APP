# Generated by Django 4.2.11 on 2024-04-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_data_engine', '0005_excel_api_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='excel',
            name='api_isactive',
            field=models.BooleanField(default=False),
        ),
    ]
