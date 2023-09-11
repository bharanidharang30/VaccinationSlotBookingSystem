# Generated by Django 4.0.6 on 2023-06-24 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0013_vaccinationregistration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinationcentre',
            name='dosages_available',
        ),
        migrations.RemoveField(
            model_name='vaccinationcentre',
            name='slots_per_day',
        ),
        migrations.RemoveField(
            model_name='vaccinationcentre',
            name='working_hours',
        ),
        migrations.AlterField(
            model_name='vaccinationcentre',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vaccinationcentre',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='VaccinationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('vaccination_centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.vaccinationcentre')),
            ],
        ),
    ]