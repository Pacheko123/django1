from django.shortcuts import render
from .models import Student, Course
from django.http import HttpResponse, Http404
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('exercise/index.html')
    get_list = Student.objects.all()
    context = {
        'name': get_list,
    }
    output = template.render(context)
    return HttpResponse(output, request)
