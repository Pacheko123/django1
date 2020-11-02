from django.shortcuts import render
from .models import Student, Course

# Create your views here.
def index(request):
    get_list = Student.Object.get('student_name')
    context = {
        'name': get_list,
    }
