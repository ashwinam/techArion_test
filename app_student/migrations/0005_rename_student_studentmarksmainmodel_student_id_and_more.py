# Generated by Django 4.1.7 on 2023-03-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_student', '0004_alter_studentmarksmainmodel_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmarksmainmodel',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='studentmarksmodel',
            old_name='student',
            new_name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentmainmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='studentmainmodel',
            name='student_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
