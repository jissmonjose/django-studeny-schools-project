from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('schools/', views.SchoolView.as_view(), name='school_view'),
    path('<int:pk>', views.SchoolDetails.as_view(), name='school_details'),
    path('create/', views.SchoolCreate.as_view(), name='school_create'),
    path('delete/<int:pk>', views.SchoolDelete.as_view(), name='school_delete'),
    path('update/<int:pk>', views.SchoolUpdate.as_view(), name='school_update'),
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('detail/<int:pk>', views.StudentDetails.as_view(), name='student_details'),
    path('create_student/', views.StudentAdd.as_view(), name='student_create'),
    path('update_student/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('delete_student/<int:pk>', views.StudentRemove.as_view(), name='student_delete'),
]
