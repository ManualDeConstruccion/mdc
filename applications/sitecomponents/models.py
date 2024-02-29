from django.db import models

class App(models.Model):
    name = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name