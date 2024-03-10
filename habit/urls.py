from django.urls import path
from habit import views
from habit.apps import HabitConfig


app_name = HabitConfig.name

urlpatterns = [
    path('', views.HabitListCreate.as_view(), name='habit-list'),
    path('<int:pk>/', views.HabitRUD.as_view(), name='habit'),
]
