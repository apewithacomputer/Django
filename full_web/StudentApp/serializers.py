from rest_framework import serializers
from .models import Classes, Students

class ClassesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classes
		fields = ('ClassId', 'ClassName')

class StudentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields = ('StudentId', 'StudentName', 'Class', 'DateOfJoining', 'PhotoFileName')