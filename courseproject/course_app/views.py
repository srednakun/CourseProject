from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = {'name': "My name is Sredna Kunowski and I am an artist."}
    
    return render(request, 'course_app/index.html', context = name)
