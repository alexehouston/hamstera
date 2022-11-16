from django.db import models

class Hamster(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    height = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'
