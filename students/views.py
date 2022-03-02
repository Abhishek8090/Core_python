from django.shortcuts import render,HttpResponse

from students.form import StudentForm

# Create your function views here.



#localhost:8000

def index(request):

    org_name="Tata Technologies Ltd"

    return render(request,'index.html',{'company':org_name})



#we are creating response for a particular request

#localhost:8000/students

def home(request):    

    #function view is sharing model and modelform details to template

    #create object of form -StudentForm

    obj=StudentForm()

    return render(request,'StudentRegisterForm.html',{'stu_form':obj})