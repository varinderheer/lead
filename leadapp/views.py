from django.shortcuts import render
from rest_framework import viewsets
from .models import NewLeads
from .serializers import NewLeadsSerializer


class NewLeadsView(viewsets.ModelViewSet): 
    queryset= NewLeads.objects.all()
    serializer_class=NewLeadsSerializer

# Create your views here.
