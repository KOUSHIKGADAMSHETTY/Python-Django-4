from django.urls import path
from student import views
urlpatterns = [
    path('<str:name>/',views.find,name='p1')
]