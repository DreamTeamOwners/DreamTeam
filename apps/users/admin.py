from django.contrib import admin
from apps.users.models import MyUser, Profile, JobPosition

admin.site.register(MyUser)
admin.site.register(Profile)
admin.site.register(JobPosition)

