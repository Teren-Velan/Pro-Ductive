
from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.delete, name='delete'),
    path('cross/<int:id>', views.cross, name='cross'),
    path('uncross/<int:id>', views.uncross, name='uncross')
]
