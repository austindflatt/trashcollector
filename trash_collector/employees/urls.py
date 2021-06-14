from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
<<<<<<< HEAD
]
=======
    path('filter/', views.daily_view, name='filter')
]
>>>>>>> 46ca6bb71856ac048275f7768f703162206944ab
