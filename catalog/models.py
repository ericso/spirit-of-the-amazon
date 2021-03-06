from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
  """Model for a Category
  """
  name = models.CharField(max_length=64)
  slug = models.SlugField(max_length=64, unique=True, help_text="Unique value for product page URL, created from name.")
  description = models.TextField()
  is_active = models.BooleanField(default=True)
  meta_keywords = models.CharField('Meta Keywords', max_length=255, help_text="Comma-delimited set of SEO keywords for meta tag")
  meta_description = models.CharField('Meta Description', max_length=255, help_text="Content for description meta tag")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    """Meta properties for Categories
    """
    db_table = 'categories'
    ordering = ['-created_at']
    verbose_name_plural = 'Categories'

  def __unicode__(self):
    """Returns a string representation of this category
    """
    return self.name

  def get_absolute_url(self):
    """Returns the canonical url for this category
    """
    return reverse('catalog_category', kwargs={'category_slug': self.slug})


class Product(models.Model):
  """Model for a Product
  """
  name = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=255, unique=True, help_text="Unique value for product page URL, created from name.")
  brand = models.CharField(max_length=64)
  sku = models.CharField(max_length=64)

  # TODO(eso) define "prices", dictionary of prices and date set
  price = models.DecimalField(max_digits=9, decimal_places=2)
  old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)

  # TODO(eso) investigate better ways of storing images
  # image = models.CharField(max_length=64)
  image = models.ImageField(upload_to='product_images')
  thumbnail = models.ImageField(upload_to='product_thumbnails')

  is_active = models.BooleanField(default=True)
  is_bestseller = models.BooleanField(default=False)
  is_featured = models.BooleanField(default=False)
  quantity = models.IntegerField()
  description = models.TextField()
  meta_keywords = models.CharField(max_length=255, help_text="Comma-delimited set of SEO keywords for meta tag")
  meta_description = models.CharField(max_length=255, help_text="Content for description meta tag")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  categories = models.ManyToManyField(Category)

  class Meta:
    """Meta properties for Products
    """
    db_table = 'products'
    ordering = ['-created_at']

  def __unicode__(self):
    """Returns a string representation of this product
    """
    return self.name

  def get_absolute_url(self):
    """Returns the canonical url for this product
    """
    return reverse('catalog_product', kwargs={'product_slug': self.slug})

  @property
  def sale_price(self):
    """Returns the product's price if it is less than the old price, else returns None
    """
    if self.old_price > self.price:
      return self.price
    else:
      return None
