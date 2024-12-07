# Generated by Django 5.1.3 on 2024-11-28 19:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_enrollments_approved_chapters'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chapters',
            new_name='Chapter',
        ),
        migrations.RenameModel(
            old_name='Enrollments',
            new_name='Enrollment',
        ),
    ]