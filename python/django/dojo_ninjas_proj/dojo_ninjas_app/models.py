from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<User Object: ({self.id} {self.name} {self.city} {self.state}{self.created_at}{self.updated_at})>"


class Ninjas(models.Model):
    dojo_id = models.ForeignKey(Dojos, related_name="Ninjas", on_delete= models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<User Object: ({self.id} {self.first_name} {self.last_name}{self.created_at}{self.updated_at})>"

