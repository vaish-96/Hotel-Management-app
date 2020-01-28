from django.urls import path
from testapp import views

app_name = 'testapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('checkin/', views.checkin,name='checkin'),
    path('guestlist/', views.guestlist,name='guestlist'),

]