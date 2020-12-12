from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('diary/<int:id>', views.show_entry, name="show_entry"),
]
