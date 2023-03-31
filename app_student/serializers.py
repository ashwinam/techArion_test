import traceback
from rest_framework import serializers
from .models import StudentMainModel, StudentMarksModel, studentMarksMainModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMainModel
        fields = '__all__'

class StudentMarksSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = StudentMarksModel
        fields = '__all__'

class StudentMarksMainSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    marks = StudentMarksSerializer()

    class Meta:
        model = studentMarksMainModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            print(validated_data)
            student = validated_data.pop('student')
            marks = validated_data.pop('marks')
            marks_student = marks.pop('student')
            std_obj = StudentMainModel.objects.create(**student)
            std_mrk_obj = StudentMainModel.objects.create(**marks_student)
            marks_obj = StudentMarksModel.objects.create(**marks)
            print(marks_obj)
            marks_obj.student_id = std_mrk_obj
            student_marks_main_obj = studentMarksMainModel.objects.create(**validated_data)
            student_marks_main_obj.student_name = std_obj
            student_marks_main_obj.marks.add(marks_obj)
            return student_marks_main_obj
        except Exception as e:
            print(traceback.format_exc())