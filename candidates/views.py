from requests import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Candidate
from .serializers import CandidateSerializer, Apply_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse


class CandidateList(ListAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        candidate = Candidate.objects.order_by('-registration_date')

        if request.accepted_renderer.format == 'html':
            data = {'candidates': candidate}
            return Response(data, template_name='resume.html')
        else:
            serializer = CandidateSerializer(candidate, many=True)
            return Response(serializer.data)


class ApplyToJob(APIView):
    def post(self, request, format=None):
        serializer = Apply_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(reverse('job:job_list'))
        return HttpResponseRedirect(status.HTTP_400_BAD_REQUEST)
