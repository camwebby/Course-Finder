from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

import operator

from .models import course1
from .forms import PostForm

def home(request):
    errorMessage = "No courses"
    Courses = course1.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)

        displayedCourses = []

        if form.is_valid():
            formData = form.cleaned_data
            for x in Courses:
                if formData["Course"].lower() in x.name.lower():
                    if x.minTariff < float(formData["Tariff"]):
                        displayedCourses.append(x)
                        displayedCourses.sort(key=operator.attrgetter('salary'))
                        displayedCourses.reverse()

            if len(displayedCourses) == 0:
                message = "No courses found"
                return render(request, 'index.html', {"msg": message})

            return render(request, 'index.html', {"COURSES": displayedCourses})

    else:
        form = PostForm()
    return render(request, 'index.html', {})



def course_detail(request, id):
    try:
        selectedCourse = course1.objects.get(id=id)
    except course.DoesNotExist:
        raise Http404("Course(s) not found")
    return render(request, "course_detail.html", {"course": selectedCourse})



def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
