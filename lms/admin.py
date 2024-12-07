from django.contrib import admin
from lms.models import Course, Enrollment, Chapter


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Enrollment)
