from django.db import models

# Create your models here.
class Club(models.Model):
	club_name = models.CharField(max_length=250)
	club_logo = models.CharField(max_length=1000)
	club_description = models.CharField(max_length=2000)

	def get_absolute_url(self):
		return reverse('clubs:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.club_name 

class Event(models.Model):
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	event_name = models.CharField(max_length=250)
	event_description = models.CharField(max_length=2000)

	def __str__(self):
		return self.event_name

