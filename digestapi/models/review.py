from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="book_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews")
    rating = models.IntegerField()
    comment = models.CharField(max_length=400)
    date_posted = models.DateField(auto_now_add=True)
