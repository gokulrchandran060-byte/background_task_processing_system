from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Job
from .serializers import JobSerializer


class JobCreateAPIView(APIView):

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job = serializer.save()
        return Response(
            JobSerializer(job).data,
            status=status.HTTP_201_CREATED
        )


class JobDetailAPIView(APIView):

    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return Response(JobSerializer(job).data)
