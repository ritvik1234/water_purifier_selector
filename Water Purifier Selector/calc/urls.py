from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name='home'),
  # path('add',views.add, name='add'),
  path('next', views.next, name= 'next'),
  path('q2', views.q2, name = 'q2'),
  path('q3', views.q3, name = 'q3'),
  path('q4', views.q4, name = 'q4'),
  path('q5', views.q5, name = 'q5'),
  path('result',views.result, name = 'result'),
  path('darcy',views.darcy, name = 'darcy'),
  path('home',views.home,name = 'home')
  ]
# ''' Here we will have a list, you will specify the mappings
# views.home pe jayenge jab bhi yeh url hoga, home fnction defined in view module'''
# t'4C8bH%qaZdFjr and Heruku(AWS Password)
