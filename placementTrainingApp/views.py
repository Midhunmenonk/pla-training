from django.shortcuts import render, redirect
from .models import auth_student, auth_faculty


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
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth_student.objects.filter(username=username, password=password).first()

        if user:
            user_id = user.id
            username = user.username
            password = user.password
            request.session['username'] = username
            return render(request, 'stud_profile.html')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    else:
        return render(request, 'login.html')
    
def faculty(request):
    if request.method == 'POST':
        user_type = request.POST.get('userType') 
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth_faculty.objects.filter(username=username, password=password).first()
        if user:
            user_id = user.id
            username = user.username
            password = user.password
            request.session['username'] = username
            return render(request, 'fac_profile.html')
        else:
            return render(request,  {'error_message': 'Invalid credentials'})

    else:
        return render(request, 'faculty.html')
        
def fac_profile(request):
    return render(request, 'fac_profile.html')

def stud_profile(request):
    return render(request, 'stud_profile.html')

def new_student(request):
    return render(request, 'new_student.html')

        
    

            
            
def profile(request):
      return render(request, 'profile.html')   

def attend(request):
     return render(request, 'attend.html')

def calendar(request):
     return render(request, 'calendar.html')  

def feedback(request):
     return render(request, 'feedback.html')   
def percentage(request):
     return render(request, 'percentage.html')




