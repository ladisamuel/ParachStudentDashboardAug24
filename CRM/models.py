from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    tutor = models.CharField(max_length=200, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)    
    price = models.IntegerField(null=True, blank=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.name)

class CourseSegment(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.course) + ' - ' + str(self.name)

class Student(models.Model):
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Others', 'Others'),
    )
    lastname =  models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    othername = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER, default=GENDER[-1], max_length=10)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    passport = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return (str(self.lastname) + ' ' + str(self.firstname))

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    courseSegment = models.ForeignKey(CourseSegment, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True, null=True)
    enddate = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.student) + ' - ' + str(self.course))

    def checkPayment(self):
        payments = StudentPayment.objects.filter(studentcourse=self)
        print('\n\nThe course payment\n\n')
        # payments = 'Hello'
        return payments

class StudentPayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.IntegerField(default=0)
    studentcourse = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)

    def totalpaid(self):
        pass
        allpayments = StudentPayment.objects.filter(id=self.id)



class Message(models.Model):
    pass