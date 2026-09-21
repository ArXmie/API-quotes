from django.db import models
from django.contrib.auth.models import User

class Quotes(models.Model):
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.quote} - {self.author}"
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
            return f"{self.name}"
    
class Quote_Category(models.Model):
    quote = models.ForeignKey(Quotes, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    
    def __str__(self):
            return f"{self.quote.quote} - {self.category.name}"
    
class Tags(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
class Quote_Tag(models.Model):
    quote = models.ForeignKey(Quotes, models.CASCADE)
    tag = models.ForeignKey(Tags, models.CASCADE)
    
    def __str__(self):
            return f"{self.quote.quote} - {self.tag.name}"

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
