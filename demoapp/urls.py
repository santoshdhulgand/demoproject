


from django.urls import path
from demoapp import views

urlpatterns = [
    path('base/' , views.BasePageView.as_view()),
    #path('read/' , views.get_student_data)
    path('read/' , views.StudentListView.as_view()),
    path('create/' , views.StudentCreateView.as_view() , name = 'student_create'),
    path('detail/<int:id>/' , views.StudentDetailView.as_view() , name = 'student_detail'),
    path('update/<int:id>/' , views.StudentUpdateView.as_view() , name = 'student_update'),
    path('delete/<int:id>/' , views.StudentDeleteView.as_view() , name = 'student_delete'),



]