from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from django.db.models import Q
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    customers = apps.get_model('customers.Customer')
    user = request.user
    try:
        logged_in_employee = Employees.objects.get(user=user)
        context = {
            'logged_in_employee': logged_in_employee
        }
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    return render(request, 'employees/index.html', context)


# Registers an employee's info
def create(request):
    if request == "POST":
        print('Triggered POST')
        user = request.user
        name = request.POST.get('name')
        zipcode = request.POST.get('zipcode')
        new_employee = Employees(user=user, name=name, zipcode=zipcode)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        print('Triggered GET')
        return render(request, 'employees/create.html')
