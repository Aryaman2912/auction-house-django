from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    """
    Model containing different attributes required.
    """
    name = models.CharField(max_length=100,verbose_name="Name")                     #Name of the auctioned product
    description = models.CharField(max_length=1000,verbose_name="Description")      #Short description of the auctioned product
    starting_bid = models.CharField(max_length=10,verbose_name="Starting bid")      #Starting bid of the auctioned product
    deadline = models.DateField(verbose_name="Deadline")                            #Deadline for auctioning of the product
    contact = models.CharField(max_length=13,verbose_name="Mobile Number")          #Contact of the owner of the product
    image = models.ImageField(upload_to='images/')                                  #Image of the product to be auctioned

    def get_absolute_url(self):
        """Returns the URL for a detail description for this product. """
        return reverse('product-detail',args=[str(self.id)])

    def __str__(self):
        """
        Method to return the name of the product.
        """
        return self.name


