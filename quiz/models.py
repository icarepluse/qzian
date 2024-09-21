from django.db import models

# Create your models here.
class tests(models.Model):
    key=models.CharField(max_length=250, null=True)
    unicid=models.CharField(max_length=250, null=True)
    user=models.CharField(max_length=250, null=True)
    totalq=models.CharField(max_length=250, null=True)
    crct=models.CharField(max_length=250, null=True)
    testids=models.CharField(max_length=250, null=True)

   
class qustion(models.Model):
    qstion=models.CharField(max_length=250, null=True)
    key=models.CharField(max_length=250, null=True)
    unicid=models.CharField(max_length=250, null=True)
  

class answer(models.Model):
    answers=models.CharField(max_length=250, null=True)
    key=models.CharField(max_length=250, null=True)
    unicid=models.CharField(max_length=250, null=True)

class optionAnser(models.Model):
    option=models.CharField(max_length=250, null=True)
    key=models.CharField(max_length=250, null=True)
    unicid=models.CharField(max_length=250, null=True)
    

class TestAnswer(models.Model):
    testkey=models.CharField(max_length=250, null=True)
    qustion=models.CharField(max_length=250, null=True)
    uanswer=models.CharField(max_length=250, null=True)
    answers=models.CharField(max_length=250, null=True)
    crect=models.CharField(max_length=250, null=True)
    
class cmuser(models.Model):
    unames=models.CharField(max_length=250, null=True)
    upass=models.CharField(max_length=250, null=True)
    umail=models.CharField(max_length=250, null=True)


