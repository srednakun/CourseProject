from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length = 10, primary_key = True)
    course_title = models.CharField(max_length = 30)
    course_description = models.CharField(max_length = 300)
    course_credit = models.IntegerField()
    course_instructor = models.CharField(max_length = 50)
    course_startDate = models.DateField()

    def _str_(self):
        return self.course_title