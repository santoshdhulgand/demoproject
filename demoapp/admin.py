from django.contrib import admin
# from appname.filename import classname/function
# from demoapp.models import Student
from .models import Student


admin.site.register(Student)

