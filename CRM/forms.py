from django.forms import Form, ModelForm
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseSegmentForm(ModelForm):
    class Meta:
        model = CourseSegment
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseForm(ModelForm):
    class Meta:
        model = StudentCourse
        # fields = '__all__'
        exclude = [
            'completed', 'enddate'
        ]
class StudentCourseEditForm(ModelForm):
    class Meta:
        model = StudentCourse
        # fields = '__all__'
        fields = [
            'completed', 'enddate'
        ]

class StudentPaymentForm(ModelForm):
    class Meta:
        model = StudentPayment
        fields = '__all__'

