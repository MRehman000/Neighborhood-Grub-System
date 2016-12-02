from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^orders-requests/$",
        views.orders_and_requests,
        name="orders_and_requests"),
    url(r"^orders/(?P<order_id>[0-9]+)/cancel/$", views.cancel_order),
    url(r"^posts/$", views.posts),
    url(r"^posts/manage/$", views.manage_posts, name="manage_posts"),
    url(r"^posts/create/$", views.create_post),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/$", views.post_detail),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/order/$", views.order_dish),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/cancel/$", views.cancel_post),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/edit/$", views.edit_post),
    url(r"^requests/$", views.requests),
    url(r"^requests/create/$", views.create_request),
    url(r"^requests/(?P<dish_request_id>[0-9]+)/$", views.request_detail),
    url(r"^requests/(?P<dish_request_id>[0-9]+)/edit/$", views.edit_request),
    url(r"^requests/(?P<dish_request_id>[0-9]+)/cancel/$", views.cancel_request),
    url(r"^chefs/(?P<chef_id>[0-9]+)/$", views.chef_detail),
]
