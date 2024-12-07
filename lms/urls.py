from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.course_list, name="home"),
    path("courses/<int:id>/", views.course_detail, name="course-detail"),
    path("test/", views.submission)
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)