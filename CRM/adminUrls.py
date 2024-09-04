from django.urls import path
from . import adminViews
urlpatterns = [
    path('', adminViews.adminHomeView, name='adminHomeUrl'),
    
    # Course
    path('courses', adminViews.courseListView, name='courseListUrl'),
    path('courses/<str:pk>/detail/', adminViews.courseDetailView, name='courseDetailUrl'),
    path('courses/schedules/<str:pk>/detail/', adminViews.courseDetailScheduleView, name='courseDetailScheduleUrl'),
    path('courses/detail/add_new_course', adminViews.createCourseViews, name='createCourseUrl'),
    
    # CourseSchedules
    path('courseschedule/list', adminViews.courseScheduleListView, name='courseScheduleListUrl'),

    # Student
    path('students', adminViews.studentListView, name='studentListUrl'),
    path('student/add-payment/<str:pk>/detail/', adminViews.studentAddPaymentView, name='studentAddPaymentUrl'),
    path('student/add-course/<str:pk>/detail/', adminViews.studentAddCourseView, name='studentAddCourseUrl'),
    path('student/edit-course/<str:pk>/detail/', adminViews.studentEditCourseView, name='studentEditCourseUrl'),
    path('student/<str:pk>/detail/', adminViews.studentDetailView, name='studentDetailUrl'),
    path('students/<str:pk>/courselists/', adminViews.studentDetailCourseView, name='studentDetailCourseUrl'),
    path('students/<str:pk>/payment_History/', adminViews.studentDetailpaymentView, name='studentDetailpaymentUrl'),
    # path('students/<str:pk>/course/', adminViews.studentCourseView, name='studentCourseUrl'),
    path('student/detail/add_new_student', adminViews.createStudentView, name='createStudentUrl'),
    path('student/<str:pk>/detail/cert', adminViews.studentCertificateView, name='studentCertificateUrl'),
    path('email/<str:pk>/cert', adminViews.emailCertificateView, name='emailCertificateUrl'),
    # path('student/detail/cert/res', adminViews.render_pdf_View, name='render_pdf_Url'),
    # render_pdf_view

    # Payments
    path('all_payment/list', adminViews.allPaymentsView, name='allPaymentsUrl'),
]



