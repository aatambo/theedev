# Generated by Django 4.0.3 on 2022-03-21 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(blank=True, null=True, upload_to='uploads/files/', validators=[django.core.validators.FileExtensionValidator(['csv'])])),
                ('min_support', models.FloatField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded'],
            },
        ),
    ]
