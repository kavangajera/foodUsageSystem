# Generated by Django 5.0.2 on 2024-02-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodutility', '0002_remove_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
