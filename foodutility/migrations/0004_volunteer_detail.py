# Generated by Django 5.0.2 on 2024-02-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodutility', '0003_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=122, null=True)),
                ('phone', models.BigIntegerField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=122, null=True)),
                ('city', models.CharField(blank=True, max_length=122, null=True)),
            ],
        ),
    ]