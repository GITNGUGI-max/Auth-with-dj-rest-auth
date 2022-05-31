
from .models import Student
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
