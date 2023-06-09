# Generated by Django 4.1.7 on 2023-03-31 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmainmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentmarksmainmodel',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='app_student.studentmainmodel'),
        ),
        migrations.AlterField(
            model_name='studentmarksmodel',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmarksmodel',
            name='sem',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], max_length=100, null=True),
        ),
    ]
