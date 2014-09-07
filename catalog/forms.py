from django import forms

from models import Product


class ProductAdminForm(forms.ModelForm):
  """Validations for Product
  """
  class Meta:
    """Meta class for ProductAdminForm
    """
    # Let our Form know what model it is associated with
    model = Product

  # Data (field) validation methods
  def clean_price(self):
    """Makes sure the price is not negative
    """
    if self.cleaned_data['price'] <= 0:
      raise forms.ValidationError('Price must be greater than zero.')
    return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
  """Adding Product to cart
  """
  quantity = forms.IntegerField(
    widget=forms.TextInput(
      attrs={
        'size': '2',
        'value': '1',
        'class': 'quantity',
        'maxlength': '5'
      }
    ),
    error_messages={
      'invalid': 'Please enter a valid quantity.'
    },
    min_value=1
  )
  product_slug = forms.CharField(widget=forms.HiddenInput())

  def __init__(self, request=None, *args, **kwargs):
    """Override the default __init__ so we can set the request
    """
    self.request = request
    super(ProductAddToCartForm, self).__init__(*args, **kwargs)

  def clean(self):
    """Custom validation to check for cookies
    """
    if self.request:
      if not self.request.session.test_cookie_worked():
        raise forms.ValidationError("Cookies must be enabled.")
      return self.cleaned_data
