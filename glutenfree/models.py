from django.db import models
 
class Glutenfree(models.Model):
    title = models.CharField(
        max_length=50
    )
    ingredients = models.TextField()

    def __str__(self): 
        return self.title
    
    