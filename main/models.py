from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='client_logos/')

    def __str__(self):
        return self.name
