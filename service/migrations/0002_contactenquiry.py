# Generated by Django 5.2.4 on 2025-07-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=70)),
                ('message', models.TextField()),
            ],
        ),
    ]
