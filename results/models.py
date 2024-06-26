from django.db import models
from subjects.models import StudentClass, Subject
from students.models import Student
from django.urls import reverse
from django.db.models import JSONField

# Create your models here.

class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = JSONField(blank=True)
    point = JSONField(blank=True)
    unit = JSONField(blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('results:declare_result')
    
    def __str__(self):
        return "%s Department-%s" % (self.select_class.class_name, self.select_class.department)