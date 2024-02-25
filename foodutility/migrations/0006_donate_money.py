# Generated by Django 5.0.2 on 2024-02-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodutility', '0005_donor_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate_Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(blank=True, max_length=122, null=True)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('reason', models.CharField(blank=True, max_length=122, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
