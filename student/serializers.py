from rest_framework import serializers
from .models import Course, Students

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	course = serializers.StringRelatedField()  # Display course name instead of ID
	class Meta:
		model = Students
		fields = '__all__'