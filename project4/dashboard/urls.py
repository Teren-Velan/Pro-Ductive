from django.urls import path
from . import views


app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='index'),
    path('cross/<int:id>', views.cross, name='cross'),
    path('uncross/<int:id>', views.uncross, name='uncross'),
    path('<int:id>/', views.delete, name='delete'),
]
