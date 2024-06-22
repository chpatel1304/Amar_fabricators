from django.db import models

# Create your models here.

class Contact(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField()
	phone=models.CharField(max_length=10,default="10")
	message=models.CharField(max_length=300)

	def __str__(self):
		return self.fullname+" - "+self.email

class Career(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField()
	phone=models.CharField(max_length=10 ,default="10")
	cv=models.FileField(upload_to="cvs/")

	def __str__(self):
		return self.fullname+" - "+self.email
