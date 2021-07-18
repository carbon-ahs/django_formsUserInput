from django.db import models

class pplData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name