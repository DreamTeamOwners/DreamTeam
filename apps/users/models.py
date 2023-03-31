from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User

from apps.users.managers import CustomUserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_company = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'


class JobPosition(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='media/profile_image/')

    experience_start_time = models.DateField(null=True, blank=True)
    experience_end_time = models.DateField(null=True, blank=True)
    experience_title = models.CharField(max_length=40, null=True, blank=True)
    experience_description = models.CharField(max_length=300, null=True, blank=True)

    education_end_year = models.DateField(null=True, blank=True)
    education_place = models.CharField(max_length=40, null=True, blank=True)
    education_title = models.CharField(max_length=40, null=True, blank=True)

    def get_completion_percentage(self):
        required_fields = ['first_name', 'job_position', 'last_name', 'phone_number', 'country', 'description', 'city', 'github','experience_start_time', 'experience_end_time', 'experience_title', 'experience_description','education_end_year', 'education_place', 'education_title', 'image']
        total_fields = len(self._meta.fields)
        completed_fields = sum(1 for field in required_fields if getattr(self, field, None))
        return int((completed_fields / len(required_fields)) * 100)


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(MyUser)
    description = models.TextField(
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name="owner_group"

    )


class Message(models.Model):
    sender = models.ForeignKey(
        MyUser,
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        related_name='messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )


class Comment(models.Model):
    username = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        "Messages",
        max_length=5000
    )
    parent = models.ForeignKey(
        'self',
        verbose_name="Parent",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children"
    )
    group = models.ForeignKey(
        Group,
        verbose_name="group",
        on_delete=models.CASCADE,
        null=True,
        related_name="reviews"
    )

