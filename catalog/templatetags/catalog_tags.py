from django import template

from django.contrib.flatpages.models import FlatPage

from cart import cart
from catalog.models import Category

register = template.Library()

@register.inclusion_tag("tags/_cart_box.html")
def cart_box(request):
  """Tag for shopping cart box
  """
  cart_item_count = cart.cart_distinct_item_count(request)
  return {
    'cart_item_count': cart_item_count
  }

@register.inclusion_tag("tags/_cart_box_menu.html")
def cart_box_menu(request):
  """Tag for shopping cart box in menu bar
  """
  cart_item_count = cart.cart_distinct_item_count(request)
  cart_items = cart.get_cart_items(request)
  return {
    'cart_item_count': cart_item_count,
    'cart_items': cart_items
  }

@register.inclusion_tag("tags/_category_list.html")
def category_list(request_path):
  """List of categories
  """
  active_categories = Category.objects.filter(is_active=True)
  return {
    'active_categories': active_categories,
    'request_path': request_path
  }


@register.inclusion_tag("tags/_footer.html")
def footer_links():
  """Footer that has links to flat pages
  """
  flatpage_list = FlatPage.objects.all()
  return {
    'flatpage_list': flatpage_list,
  }
