from django.db import models

# Create your models here.
class Instructor(models.Model):
    name= models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='media/instructors_image/')
    total_student = models.IntegerField()
    total_courses = models.IntegerField()
    facebook= models.URLField(blank=True,null=True)
    linkedin= models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name
    