from django.db import models
from instructors.models import Instructor
# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='courses_images/image/')
    description = models.TextField()
    price = models.IntegerField()
    total_students = models.IntegerField()
    total_lessons = models.IntegerField()
    total_hours = models.IntegerField()
    Instructors = models.ForeignKey(Instructor,blank=True, on_delete=models.CASCADE,default=1)
    category= models.CharField(max_length=120)
    rating = models.IntegerField()

    def __str__(self):
        return self.title
    



