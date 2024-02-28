from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name

class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accesses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')

    def __str__(self):
        return f"{self.user} -> {self.product}"
