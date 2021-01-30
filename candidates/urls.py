from django.urls import path
from .views import CandidateList, ApplyToJob

app_name = 'candidate'
urlpatterns = [
    path('', CandidateList.as_view(), name='candidate_api'),
    path('apply', ApplyToJob.as_view(), name='apply_to_job_api'),

]
