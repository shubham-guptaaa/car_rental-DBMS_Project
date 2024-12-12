# from django.urls import path,include
# from django.conf.urls import url
# from home.views import *
# from car_dealer_portal import *
# from customer_portal import *

# urlpatterns = [
#     url(r'^$',home_page),
# ]
from django.urls import path, re_path
from home.views import home_page

urlpatterns = [
    re_path(r'^$', home_page, name='home_page'),
]
