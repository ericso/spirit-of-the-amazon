from django.conf.urls.defaults import *
from ecomstore import settings


urlpatterns = patterns('',
  url(r'^register/$', 'register', {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL }, name='register'),
  url(r'^my_account/$', 'my_account', {'template_name': 'registration/my_account.html'}, name='my_account'),
  url(r'^order_info/$', 'order_info', {'template_name': 'registration/order_info.html'}, name='order_info'),
  url(r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details', {'template_name': 'registration/order_details.html'}, name='order_details'),
)

urlpatterns += patterns('django.contrib.auth.views',
  url(r'^login/$', 'login', {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL }, name='login'),
)
