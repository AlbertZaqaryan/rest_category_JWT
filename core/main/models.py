from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Category name', max_length=60)
    image = models.ImageField('Category image', upload_to='images')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-date']

class Brand(models.Model):

    category = models.ManyToManyField(Category)
    name = models.CharField('Brand name', max_length=60)
    image = models.ImageField('Brand image', upload_to='images')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['-date']

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_prod')
    name = models.CharField('Product name', max_length=70)
    price = models.PositiveIntegerField('Product price')
    image = models.ImageField('Product image', upload_to='images')
    desc = models.TextField('Product description')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-date']