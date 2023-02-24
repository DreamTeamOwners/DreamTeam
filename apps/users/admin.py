from django.contrib import admin
from apps.users.models import MyUser
from apps.users.models import Profile

admin.site.register(MyUser)
admin.site.register(Profile)

