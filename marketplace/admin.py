from django.contrib import admin
from .models import Job, JobApplication


class JobAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication)
