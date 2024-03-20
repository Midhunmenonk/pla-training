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
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)