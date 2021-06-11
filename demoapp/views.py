from django.shortcuts import render , get_object_or_404
from .models import Student
from .forms import AddStudentForm , UpdateStudentForm
from django.views.generic import (
    TemplateView , 
    View , 
    ListView,
    CreateView,
    DetailView ,
    UpdateView ,
    DeleteView
)



class BasePageView(TemplateView):
    template_name = 'demoapp/base.html'


# def get_student_data(request):
#     data = Student.objects.all()
#     return render(request , 'demoapp/read.html' , {'data':data})


# class GetStudentData(View):
#     def get(self , request , *args , **kwargs):
#         data = Student.objects.all()
#         return render(request , 'demoapp/read.html' , {'data':data})
 

class StudentListView(ListView):
    model               = Student # optional we can use model or queryset
    #queryset           = Student.objects.all() 
    template_name      = 'demoapp/read.html' # optional : default value :-> <app_name>/<modelname>_list.html
    context_object_name = 'data' # default value :-> object_list



# When we use createview modelform must be there
class StudentCreateView(CreateView):
    model               = Student
    template_name       = 'demoapp/create.html'
    fields              = "__all__" # if we use fields then there is no use of modelform
    #form_class         = AddStudentForm
    success_url         = '/read/'

    #def get_success_url(self):
        #return '/read/'

    def form_valid(self,form):
        print(form.cleaned_data) # Here we are printing the data on server wich is posted by enduser
        return super().form_valid(form)




class StudentDetailView(DetailView):
    model           = Student
    template_name   = 'demoapp/detail.html'
    # context_object_name = 'data' # default value :-> modelclassname or object
    # queryset = 

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student , id = id)


class StudentUpdateView(UpdateView): # update and createview are same
    model           = Student
    template_name   = 'demoapp/update.html'
    #fields          = '__all__'
    form_class        = UpdateStudentForm
    #success_url       = '/read/'


    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student , id = id)


    def get_success_url(self):
        return '/read/'

    def form_valid(self,form):
        print(form.cleaned_data) # Here we are printing the data on server wich is posted by enduser
        return super().form_valid(form)


class StudentDeleteView(DeleteView): # delete and detail view are same
    model           = Student
    template_name   = 'demoapp/delete.html'
    success_url     = '/read/'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student , id = id)

        
    # def get_success_url(self):
    #     return '/read/'
