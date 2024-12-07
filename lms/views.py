from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from account.forms import TestForm

from .models import Course, Enrollment


# Create your views here.
# @login_required(login_url="users/login")
def course_list(request):
    return render(request, "lms/courses.html", {"courses": Course.objects.all()})


def course_detail(request, id):
    course = Course.objects.get(pk=id)
    user = request.user
    is_enrolled = Enrollment.objects.filter(student=user, course=course).exists()
    context = {
        'course': course,
        'is_enrolled': is_enrolled
    }
    if request.method == "POST":
        enrollment = Enrollment.objects.create(course=course, student=user)
        return render(request, 'lms/course-detail.html', {'course':course})
    return render(request, "lms/course-detail.html", context)


# class CourseListView(ListView):
#     model = Course
#     queryset = Course.objects.all()
#     paginate_by = 50
#     context_object_name = "courses"
#     template_name = "lms/courses.html"


def submission(request):
    form = TestForm()
    return render(request, 'lms/test.html', {'form': form})

# def enrollment(request):
#     user = request.user()
#     print(user)