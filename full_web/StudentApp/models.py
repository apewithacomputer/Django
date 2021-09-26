from django.db import models

# Create your models here.
class Classes(models.Model):
	ClassId = models.AutoField(primary_key=True)
	ClassName = models.CharField(max_length=100)

	def __int__(self):
		return self.ClassId

class Students(models.Model):
	StudentId = models.AutoField(primary_key=True)
	StudentName = models.CharField(max_length=100)
	Class = models.CharField(max_length=100)
	DateOfJoining = models.DateField()
	PhotoFileName = models.CharField(max_length=100)

	def __int__(self):
		return self.StudentId