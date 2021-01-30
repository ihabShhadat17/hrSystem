from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'years_of_experience', 'department_ID', 'resume_file')


# Register your models here.
admin.site.register(Candidate, CandidateAdmin)
