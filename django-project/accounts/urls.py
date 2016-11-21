from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.account, name="account"),
    url(r"^signup/$", views.signup, name="signup"),
    url(r"^terminate/$", views.terminate, name="request-terminate"),
    url(r"^request-chef-permissions/$",
        views.request_chef_permissions,
        name="request-chef-permissions"),
    url(r"^suggestion/$", views.suggestion, name="suggestion"),
]
