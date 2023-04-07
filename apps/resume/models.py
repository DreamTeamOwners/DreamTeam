from django.db import models

from apps.users.models import MyUser


class Language(models.Model):
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=2, choices=(
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2')
    ))


class Skill(models.Model):
    title = models.CharField(max_length=25)


class Education(models.Model):
    title = models.CharField(max_length=25)
    degree = models.CharField(max_length=25)
    specialization = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class EmploymentCategory(models.Model):
    title = models.CharField(max_length=25)


class Experience(models.Model):
    title = models.CharField(max_length=25)
    type_employment = models.ForeignKey(
        EmploymentCategory,
        on_delete=models.PROTECT,
    )
    company_name = models.CharField(
        max_length=25
    )
    location = models.CharField(
        max_length=25
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.DateField()


class Resume(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    photo = models.ImageField(
        default='default.png',
        upload_to='media/profile_image/'
    )
    phone = models.CharField(max_length=25)
    position = models.CharField(max_length=25)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE
    )
    experience = models.ManyToManyField(
        Experience
    )
    education = models.ManyToManyField(
        Education
    )
    languages = models.ManyToManyField(Language)
