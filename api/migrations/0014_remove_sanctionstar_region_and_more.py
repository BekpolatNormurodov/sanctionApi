# Generated by Django 5.1.1 on 2024-10-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_sanctionstar_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sanctionstar',
            name='region',
        ),
        migrations.RemoveField(
            model_name='sanctionstar',
            name='shakl1',
        ),
        migrations.AddField(
            model_name='sanctionstar',
            name='starId',
            field=models.IntegerField(null=True),
        ),
    ]