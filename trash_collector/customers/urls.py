from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='register'),
    path('change_pickup_day/', views.change_pickup_day, name='change_pickup_day'),
    path('one_time/', views.one_time, name='one_time'),
    path('pickup_suspension/', views.submit_suspension, name='suspension')
]
