from django.db import models

# Create your models here.

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

SEM = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8)
]

BRANCH = [
    ('MECH', 'MECH'),
    ('CSC', 'CSC'),
    ('ECE',  'ECE'),
    ('IT', 'IT'),
    ('CIVIL', 'CIVIL')
]


class StudentMainModel(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class StudentMarksModel(models.Model):
    student = models.ForeignKey(
        StudentMainModel, on_delete=models.CASCADE, related_name='student', null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True)
    sem = models.CharField(max_length=100, choices=SEM, null=True, blank=True)




class studentMarksMainModel(models.Model):
    student = models.OneToOneField(
        StudentMainModel, on_delete=models.CASCADE, related_name='student_name', null=True, blank=True)
    marks = models.ManyToManyField(
        StudentMarksModel, related_name='student_marks')
    branch = models.CharField(max_length=100, choices=BRANCH, null=True, blank=True)
