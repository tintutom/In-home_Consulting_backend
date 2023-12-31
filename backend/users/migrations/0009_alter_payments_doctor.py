# Generated by Django 4.2.7 on 2023-11-28 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctorslot_doctor'),
        ('users', '0008_auto_20231128_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='doctors.doctorinfo'),
        ),
    ]
