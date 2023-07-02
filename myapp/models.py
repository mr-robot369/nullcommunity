from django.db import models

# Create your models here.
class UserData(models.Model):
    Name=models.CharField(max_length=50)
    Image = models.ImageField(upload_to="img/")
    Resume = models.FileField(upload_to="resume/")