from django.db import models 

class auth_student(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

class auth_faculty(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class basicUserDetailsTable(models.Model):
    reg_no = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    batch = models.PositiveIntegerField()
    branch = models.CharField(max_length = 30)
    semester = models.IntegerField()
    permanentAddress = models.CharField(max_length = 200)
    currentAddress = models.CharField(max_length = 200)
    additionalInfo = models.CharField(max_length = 500)
    profileSummary = models.CharField(max_length = 500)

class upcomingTrainingTable(models.Model):
    date = models.DateField()
    trainer = models.CharField(max_length = 20)
    time = models.TimeField()
    venue = models.CharField(max_length = 20)
    about = models.CharField(max_length = 300)

    



