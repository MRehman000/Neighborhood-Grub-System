
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden

from dishes.models import DishPost, Diner, Order, DishRequest, Chef
from dishes.forms import DishForm, DishRequestForm

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
    return redirect("orders_and_requests")

def orders_and_requests(request):
    if not request.user.is_authenticated:
        return redirect("dishes")
    else:
        diner = Diner.objects.get(user=request.user)
        orders = Order.objects.filter(diner=diner)
        requests = DishRequest.objects.filter(diner=diner)
        context = {"orders": orders, "requests": requests}
        return render(request, "dishes/orders-requests.html", context)

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
        return redirect("orders_and_requests")
    order = get_object_or_404(Order, pk=order_id)
    context = {"order": order}
    return render(request, "dishes/cancel_order.html", context)

def create_request(request):
    context = {}
    if request.method == "POST":
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            data=request.POST)
        dish_form = DishForm(prefix="dish", data=request.POST)
        if dish_request_form.is_valid() and dish_form.is_valid():
            # Create the Dish and DishRequest
            return redirect("orders_and_requests")
    else:
        dish_request_form = DishRequestForm(prefix="dish_request")
        dish_form = DishForm(prefix="dish")
    context["dish_request_form"] = dish_request_form
    context["dish_form"] = dish_form
    return render(request, "dishes/create_request.html", context)

def cancel_request(request, dish_request_id):
    if request.method == "POST":
        return redirect("orders_and_requests")
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    context = {"request": dish_request}
    return render(request, "dishes/cancel_request.html", context)
