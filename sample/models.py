from django.db import models

# Create your models here.
class Movies_pics (models.Model) :
    movie_name = models.CharField(max_length=100)
    photo = models.ImageField(default="elon2.jpg", blank=True, null=True, upload_to= "images/")

    def __str__(self) :
        return self.movie_name
    
class Director (models.Model) :
    director_name = models.CharField(max_length=100)
    director_age = models.IntegerField(null=True)

    def __str__ (self) :
        return self.director_name
    
class Actors (models.Model) :
    actor_name = models.CharField(max_length=100)
    actor_age = models.IntegerField(null=True)

    def __str__(self) :
        return self.actor_name

class Movies_list (models.Model) :
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    movie_picture = models.OneToOneField(Movies_pics, on_delete=models.SET_NULL, related_name= "movie", null=True)
    directed_by = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name= 'produced_man')
    actors = models.ManyToManyField(Actors, related_name='acted_by')

    def __str__(self) :
        return self.title