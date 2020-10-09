from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.shortcuts import redirect
# Create your views here.
#CRUD Operation

def retrieve_view(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/index.html',context=my_dict)

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    emp_list=Employee.objects.get(id=id)
    emp_list.delete()
    return redirect('/')

def update_view(request,id):
    emp_list=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp_list)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'emp_list':emp_list})
