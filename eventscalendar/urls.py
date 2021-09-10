from . import views
from django.urls import path
 
urlpatterns= [
   path("list/", views.CalendarView.as_view(), name="calendar"),
   path('register/', views.event, name='event_list'),
 
]
