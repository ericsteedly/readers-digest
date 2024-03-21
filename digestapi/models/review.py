from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=10)
    comment = models.CharField(max_length=400)
    date_posted = models.DateField()
