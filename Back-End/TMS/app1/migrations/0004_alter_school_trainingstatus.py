# Generated by Django 4.2.4 on 2023-09-01 11:23

import app1.models.enums.TrainingStatus
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_school_trainingstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='trainingStatus',
            field=models.CharField(choices=[('ONGOING', 'ONGOING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED'), ('PENDING', 'PENDING')], default=app1.models.enums.TrainingStatus.TrainingStatus['PENDING'], max_length=50),
        ),
    ]