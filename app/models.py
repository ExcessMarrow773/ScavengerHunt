from django.db import models

# Create your models here.

class requests(models.Model):
	device = models.CharField(max_length=50)
	timestamp = models.TimeField(auto_now=True)
	message = models.TextField()

	def __str__(self):
		return self.device