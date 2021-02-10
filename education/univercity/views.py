from django.shortcuts import HttpResponse
from  django.http import HttpResponse
from  .models import  Student,Tichers



def index(request):
    return HttpResponse("salom !!!!!")

def add_student(request):
    student=Student()
    student.name="fozil"
    student.group="91-20"
    student.age=19
    student.save()
    return HttpResponse('Student Added')

def student_list(request):
    students=Student.objects.all()
    for student in students:
        print(student)
    return HttpResponse("student_list")

def add_tichers(request):
    tichers=Tichers()
    tichers.name="Aziz"
    tichers.group="91"
    tichers.age=59
    tichers.save()
    return HttpResponse('Tichers Added')

def tichers_list(request):
    tichers = Tichers.objects.all()
    for ticher in tichers:
        print(ticher)
    return HttpResponse("tichers_list")