# Generated by Django 4.2.7 on 2024-01-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authenticationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='basicUserDetailsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('batch', models.PositiveIntegerField()),
                ('branch', models.CharField(max_length=30)),
                ('semester', models.IntegerField()),
                ('permanentAddress', models.CharField(max_length=200)),
                ('currentAddress', models.CharField(max_length=200)),
                ('additionalInfo', models.CharField(max_length=500)),
                ('profileSummary', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='upcomingTrainingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trainer', models.CharField(max_length=20)),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=300)),
            ],
        ),
    ]
