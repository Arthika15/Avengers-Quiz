from django.db import models

# Create your models here.
class quizquestion(models.Model):
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option1points=models.IntegerField()
    option2points=models.IntegerField()
    option3points=models.IntegerField()
    option4points=models.IntegerField()
class quizresult(models.Model):
    avengername=models.CharField(max_length=50)
    avengerdes=models.TextField()
    avengerimg=models.ImageField(upload_to="pics")
