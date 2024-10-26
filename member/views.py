from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer
# Create your views here.

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer