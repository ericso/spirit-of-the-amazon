from django import template
import locale


register = template.Library()

@register.filter(name='currency')
def currency(value):
  """Formats a value as currency based on the locale
  """
  try:
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
  except:
    locale.setlocale(locale.LC_ALL,'')
  loc = locale.localeconv()
  return locale.currency(value, loc['currency_symbol'], grouping=True)
