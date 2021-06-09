from django.db import models



class Student(models.Model):
    name            = models.CharField(max_length = 30)
    marks           = models.FloatField()
    roll_num        = models.IntegerField()


    def __str__(self):
        return self.name

        
    # def get_absolute_url(self):
    #     return '/read/'
    