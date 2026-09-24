from django.urls import path
from student import views
app_name = "student"
urlpatterns = [ 
	path("all-students",views.Allstudent,name="students"),
	path("",views.home),
	path("add-course/",views.addcourse,name="add_course"),
	path("add-student/",views.addstudent,name = "addstudent")
]