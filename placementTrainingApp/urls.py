from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('attend/', views.attend, name = 'attend'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('percentage/', views.percentage, name = 'percentage'),
    path('faculty/', views.faculty, name = 'faculty'),
    path('fac_profile/', views.fac_profile, name = 'fac_profile'),
    path('stud_profile/', views.stud_profile, name = 'stud_profile'),
    path('new_student/', views.new_student, name = 'new_student'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)