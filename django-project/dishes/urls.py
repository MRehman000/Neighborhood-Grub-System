from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^orders/$", views.orders, name="orders"),
    url(r"^orders/(?P<order_id>[0-9]+)/cancel/$", views.cancel_order),
    url(r"^orders/(?P<order_id>[0-9]+)/feedback/$", views.order_feedback),
    url(r"^posts/$", views.posts),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/$", views.post_detail),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/order/$", views.order_dish),
    url(r"^requests/$", views.requests),
    url(r"^requests/create/$", views.create_request),
    url(r"^requests/(?P<dish_request_id>[0-9]+)/$", views.request_detail),
    url(r"^requests/(?P<dish_request_id>[0-9]+)/edit/$", views.edit_request, name="requests"),
    url(r"^chefs/(?P<chef_id>[0-9]+)/$", views.chef_detail, name="chef_detail"),
    url(r"^chefs/(?P<chef_id>[0-9]+)/rate/$", views.rate_chef),
]
