from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Goal(models.Model):
    description = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    goals = models.ForeignKey(Goal)
    members = models.ForeignKey(User,on_delete=models.RESTRICT)


class Project(models.Model):
    title = models.CharField(max_length=255)
    team = models.ForeignKey(Team,on_delete=models.RESTRICT)


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('process', 'Process'),
        ('finished', 'Finished')

    )
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('middle', 'Middle'),
        ('low', 'Low')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='high')


class Board(models.Model):
    title = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project)
