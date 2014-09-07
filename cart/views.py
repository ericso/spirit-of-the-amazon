from django.shortcuts import render
from django.template import Context

import cart


def set_context(request, context_dict):
  """Sets global context vars
  """
  context = Context(context_dict)
  return context


def show_cart(request, template_name="cart/cart.html"):
  """Displays the shopping cart page
  """
  context = set_context(request, Context({
    'page_title': 'Shopping Cart',
  }))

  if request.method == 'POST':
    postdata = request.POST.copy()
    if postdata['submit'] == 'Remove':
      cart.remove_from_cart(request)
    if postdata['submit'] == 'Update':
      cart.update_cart(request)

  context['cart_items'] = cart.get_cart_items(request)
  context['cart_subtotal'] = cart.cart_subtotal(request)

  return render(request, template_name, context)
