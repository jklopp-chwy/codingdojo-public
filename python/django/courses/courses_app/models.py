from django.db import models

# Create your models here.

class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "description should be at least 15 characters"
        return errors

class course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()