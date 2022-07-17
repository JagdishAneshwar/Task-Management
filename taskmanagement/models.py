from django.db import models
from django.contrib.auth import get_user_model

class member(models.Model):
    user = models.ForeignKey(get_user_model(), name="member", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    upload = models.ImageField(upload_to='images/', null=True, blank=True)


class task(models.Model):
    user = models.ForeignKey(get_user_model(), name="task", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    due = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
    	return self.name


