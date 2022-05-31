from django import views
from django.urls import path
from .views import StudentDetail, StudentList

app_name = 'students' 
urlpatterns = [

    path('', StudentList.as_view()),
    path('<int:pk>', StudentDetail.as_view()), 
]