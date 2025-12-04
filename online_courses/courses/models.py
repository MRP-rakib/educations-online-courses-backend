from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='courses_images/image/')
    description = models.TextField()
    price = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    total_lessons = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    category= models.CharField(max_length=120)
    rating = models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



