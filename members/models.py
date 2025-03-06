from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumbr = models.IntegerField(null = True)
    age = models.IntegerField(null = True)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
