# Generated by Django 5.1.1 on 2024-09-30 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_sanctioniib'),
    ]

    operations = [
        migrations.CreateModel(
            name='SanctionIIB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('region', models.CharField(max_length=50, null=True)),
                ('shakl1', models.CharField(max_length=10, null=True)),
                ('pdf', models.FileField(null=True, upload_to='pdf/iib/')),
            ],
        ),
    ]
