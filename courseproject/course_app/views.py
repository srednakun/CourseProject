from django.shortcuts import render
from django.http import HttpResponse
from course_app.models import Course

# Create your views here.
def index(request):
    #test to print out my name
    #name = {'name': "My name is Sredna Kunowski and I am an artist."}
    #return render(request, 'course_app/index.html', context = name)

    course_list = Course.objects.order_by('course_id')
    course_dict = {'course': course_list}
    return render(request, 'course_app/index.html', context = course_dict)