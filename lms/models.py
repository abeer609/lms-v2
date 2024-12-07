from django.db import models
from django.db.models import Q
from account.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    credit = models.PositiveIntegerField()
    cover_image = models.URLField()
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to=Q(role="Teacher")
    )

    def __str__(self) -> str:
        return self.title


ATTACHMENT_TYPES = [
    ("pdf", "pdf"),
    ("img", "image"),
    ("mp4", "mp4"),
    ("ppt", "ppt"),
]


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    attachment_type = models.CharField(
        max_length=20, choices=ATTACHMENT_TYPES, blank=True, null=True
    )
    attachment = models.FileField(upload_to="attachments", blank=True, null=True)


class Enrollment(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to=Q(role="Student")
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
