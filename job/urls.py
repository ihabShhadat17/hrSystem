from django.urls import path
from .views import JobList

app_name = 'job'
urlpatterns = [
    path('', JobList.as_view(), name='job_list')
]
