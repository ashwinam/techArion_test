# Generated by Django 4.1.7 on 2023-03-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_student', '0003_alter_studentmarksmodel_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarksmainmodel',
            name='branch',
            field=models.CharField(blank=True, choices=[('MECH', 'MECH'), ('CSC', 'CSC'), ('ECE', 'ECE'), ('IT', 'IT'), ('CIVIL', 'CIVIL')], max_length=100, null=True),
        ),
    ]
