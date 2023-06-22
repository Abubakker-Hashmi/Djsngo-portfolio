from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    discription=models.TextField()
    date=models.DateField()

    def __str__(self) :
        return self.title                      #this change the object1,2 name in admin panel