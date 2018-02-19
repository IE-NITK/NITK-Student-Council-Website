from django.db import models

# Create your models here.
class Startup(models.Model):
	startup_name = models.CharField(max_length=250)
	startup_logo = models.CharField(max_length=1000)
	startup_description = models.CharField(max_length=2000)

	def get_absolute_url(self):
		return reverse('startups:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.startup_name 

class Event(models.Model):
	startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
	event_name = models.CharField(max_length=250)
	event_description = models.CharField(max_length=2000)

	def __str__(self):
		return self.event_name

