from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    students_list = Student.objects.all().prefetch_related('teacher').order_by('name')

    context = {
        'students_list': students_list,
                     }

    return render(request, template, context)
