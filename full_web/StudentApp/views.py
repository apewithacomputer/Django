from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Classes, Students
from .serializers import ClassesSerializer, StudentsSerializer
# Create your views here.

@csrf_exempt
def classApi(request):
	if request.method=='GET':
		classes = Classes.objects.all()
		classes_serializer = ClassesSerializer(classes, many=True)
		return JsonResponse(classes_serializer.data, safe=False)
	elif request.method=='POST':
		class_data=JSONParser().parse(request)
		classes_serializer=ClassesSerializer(data=class_data)
		if classes_serializer.is_valid():
			classes_serializer.save()
			return JsonResponse("Added Successfully!", safe=False)
		return JsonResponse("Failed to add",safe=False)
	elif request.method=='PUT':
		class_data=JSONParser().parse(request)
		Class = Classes.objects.get(ClassId=class_data['ClassId'])
		classes_serializer=ClassesSerializer(Class,data=class_data)
		if classes_serializer.is_valid():
			classes_serializer.save()
			return JsonResponse("Updated Successfully!", safe=False)
		return JsonResponse("Failed to update", safe=False)
	elif request.method=="DELETE":
		Class=Class.objects.get(ClassId=id)
		Class.delete()
		return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def studentApi(request):
	if request.method=='GET':
		students = Classes.objects.all()
		students_serializer = StudentsSerializer(students, many=True)
		return JsonResponse(students_serializer.data, safe=False)
	elif request.method=='POST':
		student_data=JSONParser().parse(request)
		students_serializer=StudentsSerializer(data=student_data)
		if students_serializer.is_valid():
			students_serializer.save()
			return JsonResponse("Added Successfully!", safe=False)
		return JsonResponse("Failed to add",safe=False)
	elif request.method=='PUT':
		student_data=JSONParser().parse(request)
		Student = Classes.objects.get(ClassId=student_data['StudentId'])
		students_serializer=StudentsSerializer(Student,data=student_data)
		if students_serializer.is_valid():
			students_serializer.save()
			return JsonResponse("Updated Successfully!", safe=False)
		return JsonResponse("Failed to update", safe=False)
	elif request.method=="DELETE":
		Student=Student.objects.get(ClassId=id)
		Student.delete()
		return JsonResponse("Deleted Successfully", safe=False)

