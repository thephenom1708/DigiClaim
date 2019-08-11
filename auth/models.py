from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    password_hash = models.CharField(max_length=100)

    def __str__(self):
        return self.email







