from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employees
from django.urls import reverse
from datetime import date

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    user = request.user
    try:
        logged_in_employee = Employees.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    context = {
        'logged_in_employee': logged_in_employee,
        'all_customers': all_customers,
    }
    return render(request, 'employees/index.html', context)


# Registers an employee's info
def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        zipcode = request.POST.get('zipcode')
        new_employee = Employees(user=user, name=name, zipcode=zipcode)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def daily_view(request):
    user = request.user
    logged_in_employee = Employees.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    curr_date = date.today()
    weekday = curr_date.strftime('%A')
    my_customers = []
    if request.method == "POST":
        for customer in all_customers:
            if customer.zip_code == logged_in_employee.zipcode and customer.pickup_day == weekday and customer.suspension_start == False or customer.onetime_pickup == weekday:
                my_customers.append(customer)
    return render(request, 'employees/filter.html')


def confirm_pickup(request, customer_id):
    if request.method == "POST":
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(id=customer_id)
        customer.balance += 5
        customer.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/filter.html')
