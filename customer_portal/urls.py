# from django.urls import path,include
# from customer_portal.views import *
# from django.conf.urls import url
# urlpatterns = [
#     url(r'^index/$',index),
#     url(r'^login/$',login),
#     url(r'^auth/$',auth_view),
#     url(r'^logout/$',logout_view),
#     url(r'^register/$',register),
#     url(r'^registration/$',registration),
#     url(r'^search/$',search),
#     url(r'^search_results/$',search_results),
#     url(r'^rent/$',rent_vehicle),
#     url(r'^confirmed/',confirm),
#     url(r'^manage/',manage),
#     url(r'^update/',update_order),
#     url(r'^delete/',delete_order),
# ]
from django.urls import path, re_path, include
from customer_portal.views import *

urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^auth/$', auth_view, name='auth'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^registration/$', registration, name='registration'),
    re_path(r'^search/$', search, name='search'),
    re_path(r'^search_results/$', search_results, name='search_results'),
    re_path(r'^rent/$', rent_vehicle, name='rent'),
    re_path(r'^confirmed/$', confirm, name='confirm'),
    re_path(r'^manage/$', manage, name='manage'),
    re_path(r'^update/$', update_order, name='update'),
    re_path(r'^delete/$', delete_order, name='delete'),
]
