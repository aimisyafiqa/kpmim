from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from registration.models import Mentor, Course

# Home page view
def index(request):
    return render(request, "index.html")

# Course view for displaying and saving course data
def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code, description=c_desc)
        data.save()

        course_data = Course.objects.all().values()
        context = {
            'message': 'Data Saved',
            'data': course_data,
        }

    else:
        course_data = Course.objects.all().values()
        context = {
            'message': '',
            'data': course_data,
        }

    return render(request, "course.html", context)

# Mentor view for displaying and saving mentor data
def mentor(request):
    if request.method == 'POST':
        m_code = request.POST['code']
        m_name = request.POST['name']
        data = Mentor(mentorcode=m_code, mentor_name=m_name)
        data.save()

        data = Mentor.objects.all().values()
        context = {
            'message': 'Data Saved',
            'data': data,
        }

    else:
        data = Mentor.objects.all().values()
        context = {
            'message': '',
            'data': data,
        }

    return render(request, "mentor.html", context)

# View for updating course details
def update_course(request,code):
    data=Course.objects.get(code=code)
    dict={
        'data':data
    }
    return render (request, "update_course.html", dict)


def save_update_course(request, code):
    c_desc= request.POST ['desc']
    data= Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data=Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

# View for updating mentor details
def update_mentor(request,code):
    data=Mentor.objects.get(mentorcode=code)
    dict={
        'data':data
    }
    return render (request, "update_mentor.html", dict)


def save_update_mentor(request, code):
    mname= request.POST ['name']
    data= Mentor.objects.get(mentorcode=code)
    data.mentor_name = mname
    data.save()
    return HttpResponseRedirect(reverse("mentor"))

def delete_mentor(request,code):
    data=Mentor.objects.get(mentorcode=code)
    data.delete()
    return HttpResponseRedirect(reverse('mentor'))

def search_course(request):
    if request.method == 'GET':
        #retrieve the c_code parameter and check if its not none
        c_code= request.GET.get('c_code')

        if c_code:
            data =Course.objects.filter(code=c_code.upper())
        else:
            data = None

        context ={ 
            'data':data
        }
        
        return render(request, "search_course.html", context)

    return render(request, "search_course.html")
