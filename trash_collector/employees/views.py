from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employees

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
        return render(request, 'employees/create.html')
