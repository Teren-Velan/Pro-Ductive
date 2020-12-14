from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:id>/', views.edit_entry, name="edit_entry"),
    path('daterange', views.date_range, name="daterange"),
    path('all', views.index, name='index')
]
