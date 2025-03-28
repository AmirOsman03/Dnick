# Generated by Django 4.2.20 on 2025-03-17 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('tasks_description', models.TextField()),
                ('employment_year', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('H', 'Hygienist'), ('R', 'Receptionist'), ('M', 'Manager')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('number_of_beds', models.PositiveIntegerField()),
                ('has_balcony', models.BooleanField(default=False)),
                ('cleaned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('id_image', models.ImageField(blank=True, null=True, upload_to='reservation_images/')),
                ('booking_confirmation', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(limit_choices_to={'type': 'R'}, on_delete=django.db.models.deletion.CASCADE, to='hotel_app.employee')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='room',
            field=models.ManyToManyField(blank=True, to='hotel_app.room'),
        ),
    ]
