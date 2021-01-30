from rest_framework import serializers
from .models import Candidate
from job.serializers import JobSerializer


class Apply_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'job_id', 'full_name', 'birth_date', 'years_of_experience', 'department_ID', 'resume_file')


class CandidateSerializer(Apply_Serializer):
    job_id = JobSerializer(many=False, read_only=True)
