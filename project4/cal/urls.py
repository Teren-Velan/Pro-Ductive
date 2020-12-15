from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'cal'
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    # url(r'^event/del/(?P<event_id>\d+)/$', views.del_event, name='event_del'),

    # path('event/<int:id>', views.del_event, name='del_event')
]

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>', views.event, name='event_edit'),
    path('event/del/<int:event_id>', views.del_event, name='event_del'),
]
