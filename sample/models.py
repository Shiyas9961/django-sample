from django.db import models

# Create your models here.
class Movies_pics (models.Model) :
    movie_name = models.CharField(max_length=100)
    photo = models.ImageField(default="elon2.jpg", blank=True, null=True, upload_to= "images/")

    def __str__(self):
        return self.movie_name
    
class Producer (models.Model) :
    producer_name = models.CharField(max_length=100)
    producer_age = models.IntegerField(null=True)

    def __str__ (self) :
        return self.producer_name

class Movies_list (models.Model) :
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    actor = models.CharField(max_length=50)
    movie_picture = models.OneToOneField(Movies_pics, on_delete=models.SET_NULL, related_name= "movie", null=True)
    produced_by = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, related_name= 'produced_man')

    def __str__(self):
        return self.title