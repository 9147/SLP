from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=200,unique=True)
    score = models.IntegerField(default=1000)
    members = models.ManyToManyField(User,blank=True)
    leader = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='leader')

    def __str__(self):
        return f'{self.id} {self.name}'