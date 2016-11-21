from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden

from dishes.models import DishPost, Diner, Order, DishRequest, Chef

def posts(request):
    dish_posts = DishPost.objects.all()
    context = {"dish_posts": dish_posts}
    return render(request, "dishes/posts.html", context)

def post_detail(request, dish_post_id):
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    context = {"dish_post": dish_post}
    if request.user.is_authenticated:
        context["user"] = request.user
    return render(request, "dishes/post_detail.html", context)

def order_dish(request, dish_post_id):
    diner = Diner.objects.get(user=request.user)
    dish_post = DishPost.objects.get(pk=dish_post_id)
    num_servings = request.POST["num_servings"]
    order = Order.objects.create(diner=diner,
                                 dish_post=dish_post,
                                 num_servings=num_servings)
    return redirect("orders")

def orders(request):
    if not request.user.is_authenticated:
        return redirect("dishes")
    else:
        diner = Diner.objects.get(user=request.user)
        orders = Order.objects.filter(diner=diner)
        context = {"orders": orders}
        return render(request, "dishes/orders.html", context)

def requests(request):
    dish_requests = DishRequest.objects.all()
    context = {"dish_requests": dish_requests}
    return render(request, "dishes/requests.html", context)

def request_detail(request, dish_request_id):
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    context = {"dish_request": dish_request}
    if request.user.is_authenticated:
        context["user"] = request.user
    return render(request, "dishes/request_detail.html", context)

def chef_detail(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    context = {"chef": chef}
    return render(request, "dishes/chef_detail.html", context)

def cancel_order(request, order_id):
    if request.method == "POST":
        return redirect("orders")
    order = get_object_or_404(Order, pk=order_id)
    context = {"order": order}
    return render(request, "dishes/cancel_order.html", context)
