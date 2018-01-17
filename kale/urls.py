from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('whatclass',views.whatclass,name='whatclass'),
    path('when',views.when,name='when'),
    path('howmuch',views.howmuch,name='howmuch'),
    path('travel',views.travel,name='travel'),
    path('okcool',views.okcool,name='okcool'),
    
    ]