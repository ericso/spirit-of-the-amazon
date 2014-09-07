from django.db import models
from catalog.models import Product


class CartItem(models.Model):
  """Model for a cart item.
  """
  cart_id = models.CharField(max_length=50)
  date_added = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=1)
  product = models.ForeignKey('catalog.Product', unique=False)

  class Meta:
    db_table = 'cart_items'
    ordering = ['date_added']

  @property
  def total(self):
    """The total value of the cart
    """
    return self.quantity * self.product.price

  @property
  def name(self):
    """The cart item's name
    """
    return self.product.name

  @property
  def price(self):
    """The cart item's price
    """
    return self.product.price

  def get_absolute_url(self):
    """The absolute product URL of the cart item
    """
    return self.product.get_absolute_url()

  def augment_quantity(self, quantity):
    """Add to the quantity of the item in cart
    """
    self.quantity = self.quantity + int(quantity)
    self.save()
