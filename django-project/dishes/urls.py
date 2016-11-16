from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^orders/$", views.orders, name="orders"),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/$", views.post_detail),
    url(r"^posts/(?P<dish_post_id>[0-9]+)/order/$", views.order_dish),
]
