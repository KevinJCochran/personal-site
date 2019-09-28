from django.contrib import admin

# Register your models here.
from about.models import Job, JobDetail

admin.site.register(Job)
admin.site.register(JobDetail)
