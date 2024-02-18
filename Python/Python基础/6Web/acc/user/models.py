from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=32)

    class Meta:
        db_table = "User"

    def __str__(self):
        return f'{self.id}-{self.username}-{self.password}-{self.email}'
