from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentCourse)
admin.site.register(StudentPayment)
admin.site.register(CourseSegment)
# Register your models here.
# 