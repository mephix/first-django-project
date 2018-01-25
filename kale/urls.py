from django.urls import path
from . import views

app_name = 'kale'
urlpatterns = [
    path('',views.index,name='index'),
    path('newclass/',views.newclass,name='newclass'),
    path('kalendar/',views.kalendar,name='kalendar'),
    path('myevents/',views.myevents,name='myevents'),
    path('newevent/',views.newevent,name='newevent'),
    path('myvenues/',views.myvenues,name='myvenues'),
    path('newvenue/',views.newvenue,name='newvenue'),
    ]