from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return '{},      {}'.format(self.email, self.name)


# Create your models here.
