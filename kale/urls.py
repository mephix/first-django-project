from django.urls import path
from . import views

app_name = 'kale'
urlpatterns = [
    path('',views.index,name='index'),
    
    path('findclass/',views.findclass,name='findclass'),
    path('findclass/post/',views.findclass_post,name='findclass_post'),
    path('findclass/when/<int:event_request_id>/',views.when,name='when'),
    path('findclass/when/post/<int:event_request_id>/',views.when_post,name='when_post'),
    path('findclass/howmuch/<int:event_request_id>/',views.howmuch,name='howmuch'),
    path('findclass/howmuch/post/<int:event_request_id>/',views.howmuch_post,name='howmuch_post'),
    path('findclass/travel/<int:event_request_id>/',views.travel,name='travel'),
    path('findclass/travel/post/<int:event_request_id>/',views.travel_post,name='travel_post'),
    path('findclass/okcool/<int:event_request_id>/',views.okcool,name='okcool'),
    
    path('kalendar/',views.kalendar,name='kalendar'),
    path('myevents/',views.myevents,name='myevents'),
    path('newevent/',views.newevent,name='newevent'),
    path('myvenues/',views.myvenues,name='myvenues'),
    path('newvenue/',views.newvenue,name='newvenue'),
    ]