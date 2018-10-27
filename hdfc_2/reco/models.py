from django.db import models


class property(models.Model):
	id = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=5)
	BHK = models.IntegerField()
	Price = models.FloatField(max_length=10)
	Latiutude = models.FloatField(max_length=10)
	Longitude = models.FloatField(max_length=10)
	Category = models.IntegerField()
	Area = models.FloatField()
	Balconies = models.IntegerField()
	Garden = models.IntegerField()
	Gym = models.IntegerField()
	Outdoor_sports = models.IntegerField()
	parking = models.IntegerField()
	vastu = models.IntegerField()

	def __str__(self):
		return f"{self.Name} to {self.vastu}"