from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    start_date = models.DateField('Date started')
    end_date = models.DateField('Date ended')

    def __str__(self):
        return self.company


class School(models.Model):
    school_name = models.CharField('school name', max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)
    start_date = models.DateField('Date started')
    end_date = models.DateField('Date ended')

    def __str__(self):
        return self.school_name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    technology = models.ManyToManyField(Skill)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name
