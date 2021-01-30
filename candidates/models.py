from django.db import models
from job.models import Job
# Create your models here.
from django.core.validators import FileExtensionValidator

# Create your models here.
DEPARTMENT_ID = [
    ('IT', 'IT'),
    ('HR', 'HR'),
    ('FI', 'Finance'),
]


class Candidate(models.Model):
    job_id = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=150, blank=False, null=True)
    birth_date = models.DateField()
    years_of_experience = models.PositiveIntegerField(default=0, blank=False, null=True)
    department_ID = models.CharField(max_length=2, choices=DEPARTMENT_ID, blank=False, null=True, default='IT')
    resume_file = models.FileField(upload_to='resume/',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    registration_date = models.DateTimeField(auto_now_add=True)
