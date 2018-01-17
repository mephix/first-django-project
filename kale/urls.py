from django.urls import path
from . import views

app_name = 'kale'
urlpatterns = [
    path('',views.index,name='index'),
    path('findclass/',views.findclass,name='findclass'),
    path('findclass/when/',views.when,name='when'),
    path('findclass/howmuch/',views.howmuch,name='howmuch'),
    path('findclass/travel/',views.travel,name='travel'),
    path('findclass/okcool/',views.okcool,name='okcool'),
    path('kalendar/',views.kalendar,name='kalendar'),
    path('myevents/',views.myevents,name='myevents'),
    path('newevent/',views.newevent,name='newevent'),
    path('myvenues/',views.myvenues,name='myvenues'),
    path('newvenue/',views.newvenue,name='newvenue'),
    ]