# Generated by Django 4.2.7 on 2023-11-28 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctorslot_doctor'),
        ('users', '0006_delete_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='doctor_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctorslot'),
        ),
    ]
