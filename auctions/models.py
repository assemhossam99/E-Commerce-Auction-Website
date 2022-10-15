from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 1024)
    image_url = models.CharField(max_length = 1024, blank = True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.title} -> {self.price}"

class Bid(models.Model):
    price = models.IntegerField()
    date = models.DateField()
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = "bids")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "bids", default = "")

    def __str__(self):
        return f"{self.id}: bid with value ({self.price}$) on item {self.listing.id}"

class Comment(models.Model):
    value = models.CharField(max_length = 1024)
    date = models.DateField()
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = "comments")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "comments", default = "")

    def __str__(self):
        return f"{self.id}: comment ({self.value}) on item {self.listing.id}"
