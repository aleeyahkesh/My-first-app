from django.shortcuts import get_object_or_404, redirect, render
from emp.forms import EmployeeForm
from emp.models import Employee 
#from django.core.urlresolvers import reverse
#reverse('emp_myview', args=())

# Create your views here.

def home(request):
    return render(request, 'emp/home.html')

def allemployees(request):
    employees = Employee.objects.all()
    dict = {'allemployees': employees}
    return render(request, 'emp/allemployees.html', context=dict)

def employeedetails(request, id):
    employee = Employee.objects.get(id=id)
    dict = {'employee': employee}
    return render(request, 'emp/employeedetails.html', context=dict)

def employeedelete(request, id):
    employee = Employee.objects.get(id=id)
    #employee = Employee.objects.select_related('empDept', 'empCountry').all().filter(id=id)
    dict = {'employee': employee}

    if request.method == 'POST':
        employee.delete()
        return redirect('allemployees')

    return render(request, 'emp/employeedelete.html', context=dict)

def employeeUpdate(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)

    #form = EmployeeForm(request.POST, instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)# instance=emp)
        if form.is_valid():
            form.save()
        return redirect('allemployees')
    dict = {'form': form}
    
    return render(request, 'emp/updateemployee.html', context=dict)

def addemployee(request):
    form = EmployeeForm()
    dict = {'form': form}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('allemployees')

    return render(request, 'emp/addemployee.html', dict)

def doupdateemployee(request):
    form = EmployeeForm()
    dict = {'form': form}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('allemployees')

    return render(request, 'emp/updateemployee.html', dict)
    


