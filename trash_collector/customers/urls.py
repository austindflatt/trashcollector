from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='register_new_customer'),
    path('one_time_pickup/', views.one_time_pickup, name='one_time'),
    path('pickup_suspension/', views.submit_suspension, name='suspension')
]
