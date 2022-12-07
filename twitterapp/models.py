from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
from accounts.models import CustomUser
# Create your models here.
class feature(models.Model):
    name= models.CharField(max_length=255)
    purchaser=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    discription=models.TextField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail',args=[self.id])