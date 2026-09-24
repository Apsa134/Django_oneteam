from django.db import models

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=30)

	def __str__(self):
		return self.course_name

class Students(models.Model):
	std_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	dob = models.DateField()
	address = models.CharField(max_length=300)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)

	def __str__(self):
		return self.std_name