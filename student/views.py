from django.shortcuts import render,redirect
from student.models import Course,Students
from django.contrib import messages


# Create your views here.
def Allstudent(request):
    course = "Python Django"
    students = Students.objects.all()
    return render(request,"all_students.html",{"my_course":course, "all_stud":students})

def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,"index.html",{"all_course":courses})

def addcourse(request):
    if request.method == 'POST':
        course_value =request.POST['course']
        Course(course_name = course_value).save()    # here we save the course name what the user gave
        return redirect("/") 
    return render(request,"add_course.html")

def addstudent(request):
    courses = Course.objects.all()
    if request.method =='POST':
       student_name = request.POST['std_name']
       ph_num = request.POST['phone']
       dob =request.POST['dob']
       stud_address = request.POST['address']
       course = request.POST['course']
       course_value = Course.objects.get(id=course)
       Students(std_name=student_name,phone=ph_num,dob=dob,address=stud_address,course=course_value).save()
       messages.info(request,"New Student added successfully")
       return redirect("student:students")
    return render(request,"add_student.html",{"all_course":courses})