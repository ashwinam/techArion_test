# Generated by Django 4.1.7 on 2023-03-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_student', '0005_rename_student_studentmarksmainmodel_student_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmarksmainmodel',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studentmarksmodel',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='studentmainmodel',
            name='student_id',
        ),
        migrations.AddField(
            model_name='studentmainmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
