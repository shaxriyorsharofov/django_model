from  django.urls import  path
from . import views
urlpatterns=[
    path('univercity/',views.index,name='index'),
    path('add_student/',views.add_student,name="add-student"),
    path('student_list/',views.student_list,name='student_list'),
    path('add_tichers/', views.add_tichers, name='add_tichers'),
    path('tichers_list/',views.tichers_list,name='tichers_list')

]