from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from curriculum.models import Lesson
from instructors.models import Instructor
from courses.serializers import CourseSerializer
from instructors.serializer import InstructorSerializer
from curriculum.serializer import LessonSerializer
# Create your views here.




class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

