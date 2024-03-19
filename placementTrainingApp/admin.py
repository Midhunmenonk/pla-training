from django.contrib import admin
from .models import auth_faculty, auth_student, basicUserDetailsTable, upcomingTrainingTable
# Register your models here.
admin.site.register(auth_student)
admin.site.register(auth_faculty)
admin.site.register(basicUserDetailsTable)
admin.site.register(upcomingTrainingTable)
