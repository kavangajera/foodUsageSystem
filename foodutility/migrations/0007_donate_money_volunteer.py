# Generated by Django 5.0.2 on 2024-02-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodutility', '0006_donate_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate_money',
            name='volunteer',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
