from django.db import models


class ImageMessage(models.Model):
    image = models.ImageField(upload_to='usr')