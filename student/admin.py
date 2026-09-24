from django.contrib import admin

# Register your models here.
from student.models import Course,Students

admin.site.register(Course)
admin.site.register(Students)