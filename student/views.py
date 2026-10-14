from django.shortcuts import render,redirect
from student.models import Course,Students,Trainer
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
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

class AddTrainer(CreateView):
    template_name = "add-trainer.html"
    model = Trainer
    fields = "__all__"
    success_url = '/'

class TrainerList(ListView):
    model = Trainer
    template_name = 'trainer_list.html'
    context_object_name = 'trainers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for trainer in context['trainers']:
            trainer.details = [
                (field.verbose_name, field.value_from_object(trainer))
                for field in trainer._meta.fields
                if field.name != 'profile_pic'
            ]

        return context

class EditTrainer(UpdateView):
    model = Trainer
    fields = '__all__'
    template_name = 'edit_trainer.html'
    success_url = reverse_lazy('student:trainer_list')

class DeleteTrainer(DeleteView):
    model = Trainer
    success_url = reverse_lazy("student:home")
    