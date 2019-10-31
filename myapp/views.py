from django.shortcuts import render
# import views
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, School
from django.urls import reverse_lazy


# Create your views here.
# class based views

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # context is a dictionary can pass any no of
        context = super().get_context_data(**kwargs)
        context['name'] = 'jiss'
        return context


# list view
class SchoolView(ListView):
    model = School


# details view
class SchoolDetails(DetailView):
    model = School
    context_object_name = 'school_data'
    template_name = 'myapp/school_detail.html'


# create view
class SchoolCreate(CreateView):
    fields = ['name', 'location', 'principal']
    model = School


# update view

class SchoolUpdate(UpdateView):
    fields = ('location', 'principal')
    model = School


# delete view
class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy('myapp:school_view')


# list students
class StudentList(ListView):
    model = Student


# student details
class StudentDetails(DetailView):
    model = Student
    context_object_name = 'student_data'
    template_name = 'myapp/student_detail.html'


# add students
class StudentAdd(CreateView):
    fields = ['name', 'age', 'school']
    model = Student


# student update
class StudentUpdate(UpdateView):
    fields = '__all__'
    model = Student


# student Delete
class StudentRemove(DeleteView):
    model = Student
    success_url = reverse_lazy('myapp:student_list')

