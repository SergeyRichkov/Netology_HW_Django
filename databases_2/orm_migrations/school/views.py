from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    students_list = Student.objects.all().prefetch_related('teacher')

    for a in students_list:
        print(a.teacher.all())


    context = {
        'students_list': students_list,
                     }

    return render(request, template, context)
