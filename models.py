from django.db import models
class UserDetails(models.Model):
    userid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.TextField()
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.name






