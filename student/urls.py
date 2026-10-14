from django.urls import path
from student import views
app_name = "student"
urlpatterns = [ 
	path("all-students",views.Allstudent,name="students"),
	path("",views.home),
	path("add-course/",views.addcourse,name="add_course"),
	path("add-student/",views.addstudent,name = "addstudent"),
	path("add-trainer/",views.AddTrainer.as_view(),name="add-trainer"),
	path('trainers/', views.TrainerList.as_view(), name='trainer_list'),
	path('trainers/<int:pk>/edit/', views.EditTrainer.as_view(), name='edit_trainer'),
	path('trainer-delete/<int:pk>',views.DeleteTrainer.as_view(),name = 'delete_trainer'),

]