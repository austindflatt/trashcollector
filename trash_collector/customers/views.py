from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    try:
        logged_in_customer = Customer.objects.get(user=user)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customers:register'))
    return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        user = request.user
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        pickup_day = request.POST.get('pickup_day')
        new_customer = Customer(fname=fname, lname=lname, address=address, zip_code=zip_code, user=user,
                                pickup_day=pickup_day)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/register.html')


# Allows customer to request a one time pickup
def one_time_pickup(request):
    if request.method == "POST":
        pickup_day = request.POST.get('pickup_day')
        temp_pickup = Customer(pickup_day=pickup_day)
        temp_pickup.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/one_time.html')


# Allows customers to request a temporary stop in service and to request a service continuation start date
def submit_suspension(request):
    if request.method == "POST":
        suspension_stop = request.POST.get('suspension_stop')
        suspension_start = request.POST.get('suspension_start')
        temp_stop = Customer(suspension_stop=suspension_stop, suspension_start=suspension_start)
        temp_stop.save()
        return HttpResponseRedirect(reverse('customers:index.html'))
    else:
        return render(request, 'customers/suspension.html')
