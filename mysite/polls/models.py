from django.db import models
from django.core.exceptions import ValidationError

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text

class Signup(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200,unique=True)
	password = models.CharField(max_length=200)
	phone_num = models.CharField(max_length=200)
	def __str__(self):
		return self.first_name + " " + self.last_name

class Patient(models.Model):
	doctor_name = models.ForeignKey(Signup, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200,default='sharath')
	last_name = models.CharField(max_length=200,default='sharath')
	email = models.CharField(max_length=200,default='sharath@gmail.com')
	phone_num = models.CharField(max_length=200,default='123')
	blood_type = models.CharField(max_length=200,default='O+')
	height = models.CharField(max_length=200,default='175')
	weight = models.CharField(max_length=200,default='50')
	def clean(self):
		if self.doctor_name != "sharath":
			raise ValidationError(_('Draft entries may not have a publication date.'))
	def __str__(self):
		return self.first_name + " " + self.last_name




