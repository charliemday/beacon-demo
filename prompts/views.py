from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from .models import PromptLog
from .serializers import PromptLogSerializer


class PromptLogListCreateView(ListCreateAPIView):

    queryset = PromptLog.objects.all()
    serializer_class = PromptLogSerializer
