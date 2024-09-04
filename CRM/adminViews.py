from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def adminHomeView(r):
    students = Student.objects.all()
    context = {
        'students': len(students)
    }
    return render(r, 'admin/dashboardpage.html', context)

def createCourseViews(r):
    form = CourseForm
    if r.method == 'POST':
        form = CourseForm(r.POST)
        if form.is_valid:
            course = Course(
                name=r.POST.get('name'),
                tutor=r.POST.get('tutor'),
                price=r.POST.get('price'),
                details=r.POST.get('details'),
                )
            course.save()
            course = Course.objects.get(id=course.id)
            messages.success(r, 'Course created successfully')
            return redirect('courseDetailUrl', course.id)

    return render(r, 'admin/course/createNewCourse.html', {'form':form})

def courseListView(r):
    return render(r, 'admin/course/courseList.html', {'courses': Course.objects.all()})

def courseDetailView(r, pk):
    course = Course.objects.get(id=pk)
    coursesegment = CourseSegment.objects.filter(course=course)
    students = StudentCourse.objects.filter(course=course)

    context = {
        'course': course,
        'students': students,
        'courseSegment':coursesegment
        }
    return render(r, 'admin/course/courseDetail.html', context)

def courseDetailScheduleView(r, pk):
    course = Course.objects.get(id=pk)
    coursesegment = CourseSegment.objects.filter(course=course)
    students = StudentCourse.objects.filter(course=course)
 
    courseScheduleForm = CourseSegmentForm
    if r.method == 'POST':
        courseScheduleForm = CourseSegmentForm(r.POST)
        if courseScheduleForm.is_valid:
            c_segment = CourseSegment(name=r.POST.get('name'), course=course)
            c_segment.save()
            messages.success(r, 'Course created successfully')
            return redirect('courseDetailScheduleUrl', pk)
    
    context = {
        'courseScheduleForm': courseScheduleForm,
        'course': course,
        'students': students,
        'courseSegment':coursesegment,
        }
    return render(r, 'admin/course/courseDetailSchedule.html', context)


def courseScheduleListView(r):
    return render(r, 'admin/courseSchedule/courseScheduleList.html', {'schedules': CourseSegment.objects.all()})



# Students
def createStudentView(r):
    form = StudentForm
    if r.method == 'POST':
        form = StudentForm(r.POST)
        if form.is_valid:
            student = Student(
                lastname = r.POST.get('lastname'),
                firstname = r.POST.get('firstname'),
                othername = r.POST.get('othername'),
                phonenumber = r.POST.get('phonenumber'),
                email = r.POST.get('email'),
                gender = r.POST.get('gender'),
                passport = r.POST.get('passport'),
            )
            student.save()
            studentObject = Student.objects.get(id=student.id)
            messages.success(r, 'Student created successfully')
            return redirect('studentDetailUrl', studentObject.id)

    return render(r, 'admin/student/createNewStudent.html', {'form':form})

def studentListView(r):
    return render(r, 'admin/student/studentList.html', {'students': Student.objects.all()})

def studentDetailView(r, pk):
    try:
        student = Student.objects.get(id=pk)
    except:
        return redirect('studentListUrl')

    allCourses = Course.objects.all()
    CourseSchedule = []
    for course in allCourses:
        addnewschedule = CourseSegment.objects.filter(course=course)

        if addnewschedule:
            CourseSchedule.append(addnewschedule.last())

    student_courses = StudentCourse.objects.filter(student=student)

    for eachItem in CourseSchedule:
        for eachStudentcourse in student_courses:
            if eachStudentcourse.courseSegment.course == eachItem.course:
                CourseSchedule.pop(CourseSchedule.index(eachItem))
                pass

    context = {
        'paymentForm': StudentPaymentForm,
        'courseForm': StudentCourseForm,
        'allCourses': allCourses,
        'courses': student_courses,
        'student': student,
        'courseSegment': CourseSchedule,
        }
    return render(r, 'admin/student/studentDetail.html', context)

def studentAddCourseView(r, pk):

    student = Student.objects.get(id=pk)
    courseSegment = CourseSegment.objects.get(id=r.POST.get('courseSegment'))
    course = Course.objects.get(id=courseSegment.course.id)
    form = StudentCourseForm
    if r.method == 'POST':
        form = StudentCourseForm(r.POST)
        if form.is_valid:
            studentCourse = StudentCourse.objects.create(
            student = student,
            course = courseSegment.course,
            courseSegment = courseSegment,
            )
            studentCourse.save()
            messages.success(r, 'Course registered successfully')
            return redirect('studentDetailUrl', pk)

def studentEditCourseView(r, pk):
    form = StudentCourseEditForm

def studentDetailCourseView(r, pk):
    try:
        student = Student.objects.get(id=pk)
        courses = StudentCourse.objects.filter(student=student)
    except:
        print('Student does not exit')
        messages.info(r, 'Student does not exits')
        return redirect('studentListUrl')


    if r.method == 'POST':
        try:
            course_id = r.POST.get('id')
            course = StudentCourse.objects.get(id=course_id)
            form = StudentCourseEditForm(r.POST, instance=course)
            
            if form.is_valid:
                form.save()
                messages.success(r, 'Course completed successfully')
                return redirect('studentDetailCourseUrl', course.student.id)

        except:
                messages.error(r, 'Error Occured...!!!')
                return redirect('studentDetailCourseUrl', course.student.id)
            

    context = {
        'courses': courses,
        'student': student,
        }
    return render(r, 'admin/student/studentDetailCourse.html', context)

def studentAddPaymentView(r, pk):
    form = StudentPaymentForm
    if r.method == 'POST':
        form = StudentPaymentForm(r.POST)
        if form.is_valid:
            payment = StudentPayment(
                student = Student.objects.get(id=pk),
                studentcourse = StudentCourse.objects.get(id=r.POST.get('studentcourse')),
                payment = r.POST.get('payment'),
                )
            payment.save()
            messages.success(r, 'Payment successfully made')
            return redirect('studentDetailUrl', pk)


def studentDetailpaymentView(r, pk):
    try:
        student = Student.objects.get(id=pk)
        payments = StudentPayment.objects.filter(student=student)
    except:
        print('Student does not exit')
        messages.info(r, 'Student does not exits')
        return redirect('studentListUrl')
    
    for payment in payments:
        print(payment.studentcourse.checkPayment(), "\n\n\n")

    context = {
        'payments': payments,
        'student': student,
        }
    return render(r, 'admin/student/studentDetailPayment.html', context)

def studentCertificateView(r, pk):
    # student = Student.objects.get(id=pk)
    course = StudentCourse.objects.get(id=pk)
    return render(r, 'admin/student/certificate/student/studentCert.html', {'course':course })

def emailCertificateView(r, pk):
    course = StudentCourse.objects.get(id=pk)
    

    email = EmailMessage(
        "Hello",
        "Body goes here",
        "from@example.com",
        ["to1@example.com", "to2@example.com"],
        ["bcc@example.com"],
        reply_to=["another@example.com"],
        headers={"Message-ID": "foo"},
    )
    # message.attach_file("/images/weather_map.png")
    return render(r, 'emailCertificateTemplate.html')


# import magic
# import os
# from django.core.mail import EmailMessage

# def send_email_with_attachment(subject, message, from_email, recipient_list, attachment_path):
#     with open(attachment_path, 'rb') as file:
#         file_content = file.read()

#     mime_type = magic.from_buffer(file_content, mime=True)

#     # Extract the filename from the attachment_path
#     file_name = os.path.basename(attachment_path)

#     email = EmailMessage(subject, message, from_email, recipient_list)
#     email.attach(file_name, file_content, mime_type)

#     # Send the email
#     email.send()

def allPaymentsView(r):
    return render(r, 'admin/payment/paymentList.html', {'allPayments': StudentPayment.objects.all()})
     







# email_utils.py

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                        return uri

        # make sure that file exists
        if not os.path.isfile(path):
                raise RuntimeError(
                        'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

