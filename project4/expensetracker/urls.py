from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.edit_entry, name="edit_entry"),
    path('daterange', views.date_range, name="daterange"),
    path('dashboard', views.dashboard, name='dashboard')
]
