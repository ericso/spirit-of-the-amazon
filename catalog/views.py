from django.core import urlresolvers
from django.shortcuts import (
  get_object_or_404,
  render
)
from django.template import Context
from django.http import HttpResponseRedirect

from config.settings import SITE_NAME

from models import (
  Category,
  Product,
)
from forms import ProductAddToCartForm

# from cart.cart import add_to_cart
from cart import cart


def set_context(request, context_dict):
  """Sets global context vars
  """
  context = Context(context_dict)
  return context


def catalog_home(request, template_name='catalog/catalog_page.html'):
  """Renders the catalog home view
  """

  context = set_context(request, Context({
    'page_title': SITE_NAME,
    'categories': Category.objects.all(),
  }))

  return render(request, template_name, context)


def show_category(request, category_slug, template_name='catalog/category_page.html'):
  """Renders the category view
  """
  category = get_object_or_404(Category, slug=category_slug) # Get Category from slug

  # Set view context
  context = set_context(request, {
    'category': category,
    'products': category.product_set.all(), # Get products from category
    'page_title': category.name,
    'meta_keywords': category.meta_keywords,
    'meta_description': category.meta_description,
  })

  return render(request, template_name, context)


def show_product(request, product_slug, template_name="catalog/product_page.html"):
  """Renders the product view, on POST adds product to cart
  """
  p = get_object_or_404(Product, slug=product_slug)
  context = set_context(request, {
    'product': p,
    # 'categories': p.categories.filter(is_active=True),
    'categories': p.categories.all(),
    'page_title': p.name,
    'meta_keywords': p.meta_keywords,
    'meta_description': p.meta_description,
  })

  if request.method == 'POST':
    # add to cart...create the bound form
    postdata = request.POST.copy()
    form = ProductAddToCartForm(request, postdata)

    # check if posted data is valid
    if form.is_valid():
      # add to cart and redirect to cart page
      cart.add_to_cart(request)

      # if test cookie worked, get rid of it
      if request.session.test_cookie_worked():
        request.session.delete_test_cookie()

      # redirect user to cart view
      url = urlresolvers.reverse('show_cart')
      return HttpResponseRedirect(url)
  else:
    # GET request, note the request as a kwarg
    form = ProductAddToCartForm(request=request, label_suffix=':')

  # assign the hidden input the product slug
  form.fields['product_slug'].widget.attrs['value'] = product_slug

  # add form to context
  context['form'] = form

  # set the test cookie on our first GET request
  request.session.set_test_cookie()

  return render(request, template_name, context)


def file_not_found_404(request):
  """Custom 404 not found error view
  """
  context = set_context(request, {
    page_title: 'Page Not Found'
  })

  return render(request, 'catalog/404.html', context)

