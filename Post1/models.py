from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cash = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post',kwargs={'pk':self.pk})

