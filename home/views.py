from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

