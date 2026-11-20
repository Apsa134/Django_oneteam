from django.urls import path,include
from student import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

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
	path('api/courses/', views.CourseList.as_view(), name='course_list'),
	path('api/courses/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
	path('api/', include(router.urls)),

	
]