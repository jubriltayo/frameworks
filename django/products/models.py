from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=128) # map to database
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10000, decimal_places=2)
    summary     = models.TextField()
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        """ auto-generate url for products """
        # return f"/product/{self.id}"  # this is hard coding though
        
        # for dynamic url
        return reverse("products:product-detail", kwargs={"my_id": self.id})
