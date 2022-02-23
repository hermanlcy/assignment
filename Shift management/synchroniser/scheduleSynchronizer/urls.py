from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.home, name='home'),
    path('guide', views.guide, name='guide'),
    # TEMPORARY
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('calendar', views.calendar, name='calendar'),
    path('shift', views.shift, name='shift'),
    path('delete_incorrect_shifts', views.delete_incorrect_shifts,
         name='delete_incorrect_shifts'),
    path('search_function', views.search_function, name='search_function'),
    path('delete_by_id', views.delete_by_id, name='delete_by_id'),

    path('callback', views.callback, name='callback'),

    path('calendar/new', views.newevent, name='newevent'),
]
