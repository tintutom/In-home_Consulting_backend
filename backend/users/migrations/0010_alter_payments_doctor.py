# Generated by Django 4.2.7 on 2023-11-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctorslot_doctor'),
        ('users', '0009_alter_payments_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='doctors.doctorinfo'),
        ),
    ]
