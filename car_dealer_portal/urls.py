# from django.urls import path,include
# from car_dealer_portal.views import *
# from django.conf.urls import url

# urlpatterns = [
#     url(r'^index/$',index),
#     url(r'^login/$',login),
#     url(r'^auth/$',auth_view),
#     url(r'^logout/$',logout_view),
#     url(r'^register/$',register),
#     url(r'^registration/$',registration),
#     url(r'^add_vehicle/$',add_vehicle),
#     url(r'^manage_vehicles/$',manage_vehicles),
#     url(r'^order_list/$',order_list),
#     url(r'^complete/$',complete),
#     url(r'^history/$',history),
#     url(r'^delete/$',delete),
# ]
from django.urls import path, re_path
from car_dealer_portal.views import *

urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^auth/$', auth_view, name='auth'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^registration/$', registration, name='registration'),
    re_path(r'^add_vehicle/$', add_vehicle, name='add_vehicle'),
    re_path(r'^manage_vehicles/$', manage_vehicles, name='manage_vehicles'),
    re_path(r'^order_list/$', order_list, name='order_list'),
    re_path(r'^complete/$', complete, name='complete'),
    re_path(r'^history/$', history, name='history'),
    re_path(r'^delete/$', delete, name='delete'),
]
