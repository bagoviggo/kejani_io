from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Add more fields as needed

    def __str__(self):
        return self.name

class Property(models.Model):
    CITY_CHOICES = (
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        # Add more cities as needed
    )
    
    CATEGORY_CHOICES = (
        ('1', '1 Bedroom'),
        ('2', '2 Bedroom'),
        ('3', '3 Bedroom'),
        ('B', 'Bungalow'),
        ('F', 'Flat'),
        # Add more categories as needed
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class PropertyListing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    # Add more fields for the property listing as needed

    def __str__(self):
        return self.property.title
