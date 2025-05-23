from django.db import models
from django.urls import reverse

  

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True
                            )

    objects = models.Manager()

    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


 
    def __str__(self):
        return self.name




class Product(models.Model):

    class Status(models.TextChoices): 
        DRAFT = 'DF', 'Draft'
        AVAILABLE = 'AV', 'Available'

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, blank=True, null=True)

    
    
 
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
 
 
    class Meta:
       ordering = ['name']
       indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-available']),
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.name

    objects = models.Manager()
