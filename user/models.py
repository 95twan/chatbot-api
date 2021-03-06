from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128, null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
