from django.db import models

# Create your models here.

class request(models.Model):
	device = models.CharField(max_length=50)
	message = models.TextField()
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.device

class Clue(models.Model):
	title = models.CharField(max_length=50)
	clue_body = models.TextField()
	created_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)