from django.shortcuts import render
from .models import auth_faculty, auth_student


# Create your views here.

def register(request):
    render(request, 'register.html')
    if request.method == 'POST':
        reg_no = request.POST.get('registerNumber')
        password = request.POST.get('password')
        user = request.POST.get('userType')
        if user == 'faculty':
              auth_faculty(reg_no = reg_no, password = password).save()
        else:
              auth_student(reg_no = reg_no, password = password).save()
        return render(request, 'login.html')
    else:
         return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_type = request.POST.get('userType') 
        reg_no = request.POST.get('registerNumber')
        password = request.POST.get('password')

        if user_type == 'faculty':
            user = auth_faculty.objects.filter(reg_no=reg_no, password=password).first()
        elif user_type == 'student':
            user = auth_student.objects.filter(reg_no=reg_no, password=password).first()

        if user:
            user_id = user.id
            reg_no = user.reg_no
            password = user.password
            request.session['registerNumber'] = reg_no
            return render(request, 'profile.html')
        else:
            return render(request, 'index.html', {'error_message': 'Invalid credentials'})

    else:
        return render(request, 'index.html')
            
            
def profile(request):
      return render(request, 'profile.html')   

def attend(request):
     return render(request, 'attend.html')

def calendar(request):
     return render(request, 'celander.html')  

def feedback(request):
     return render(request, 'feedback.html')   

def percentage(request):
     return render(request, 'percentage.html')
