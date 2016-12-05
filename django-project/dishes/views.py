from django.shortcuts import get_object_or_404, render, redirect

from dishes.models import (
    DishPost, Diner, Order, DishRequest, Chef,
    OrderFeedback, RateChef, RateDiner, Dish
)
from dishes.forms import DishForm, DishRequestForm, DishPostForm, ChefForm
from dishes.forms import FeedbackForm, RateChefForm, RateDinerForm

def posts(request):
    dish_posts = DishPost.objects.filter(status=DishPost.OPEN)
    is_chef = hasattr(request.user, "chef")
    context = {"dish_posts": dish_posts, "is_chef": is_chef}
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
        diner = request.user.diner

        pending_orders = diner.order_set.filter(status=Order.OPEN)
        closed_orders = diner.order_set.filter(status__gt=Order.OPEN)

        diner_requests = diner.dishrequest_set
        pending_requests = diner_requests.filter(status=DishRequest.OPEN)
        closed_requests = diner_requests.filter(status__gt=DishRequest.OPEN)

        is_chef = hasattr(request.user, "chef")

        context = {
            "orders": pending_orders,
            "has_history": closed_orders.count() or closed_requests.count(),
            "requests": pending_requests,
            "is_chef": is_chef
        }
        return render(request, "dishes/orders-requests.html", context)

def orders_and_requests_history(request):
    if not request.user.is_authenticated:
        return redirect("dishes")
    else:
        diner = request.user.diner

        orders = diner.order_set.filter(status__gt=Order.OPEN)
        requests = diner.dishrequest_set.filter(status__gt=DishRequest.OPEN)

        context = {
            "orders": orders,
            "requests": requests
        }

        return render(request, "dishes/orders-requests-history.html", context)

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
    open_dish_posts = chef.dishpost_set.filter(status=DishPost.OPEN)
    has_history = open_dish_posts.count() < chef.dishpost_set.count()
    context = {
        "chef": chef,
        "open_dish_posts": open_dish_posts,
        "has_history": has_history,
    }
    return render(request, "dishes/chef_detail.html", context)

def chef_history(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    past_dish_posts = chef.dishpost_set.filter(status=DishPost.COMPLETE)
    context = {
        "chef": chef,
        "past_dish_posts": past_dish_posts,
    }
    return render(request, "dishes/chef_history.html", context)

def rate_chef(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    if request.method == "POST":
        form = RateChefForm(request.POST)
        if form.is_valid():
            int_rating = request.POST["rating"]
            rating = RateChef.objects.create(chef, rating=int_rating)
        else:
            form = RateChefForm()
    return redirect(request, "dishes/rate_chef.html")

def order_feedback(request, order_id):
    context = {}
    order = get_object_or_404(Order, pk=order_id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            OrderFeedback.objects.create(**form.cleaned_data)
            context["feedback_submitted"] = True
        else:
            form = FeedbackForm()
        context["form"] = form
        return render(request, "dishes/orders.html", context)


def cancel_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, pk=order_id)
        if request.user == order.diner.user:
            order.status = Order.CANCELLED
            order.save()
        return redirect("orders_and_requests")
    order = get_object_or_404(Order, pk=order_id)
    context = {"order": order}
    return render(request, "dishes/cancel_order.html", context)

def create_request(request):
    context = {}
    if request.method == "POST":
        dish_form = DishForm(prefix="dish", data=request.POST)
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            data=request.POST)
        if dish_request_form.is_valid() and dish_form.is_valid():
            # Bind some more programmer friendly references
            diner = request.user.diner
            dish_request_form_data = dish_request_form.cleaned_data

            # Create the Dish
            # The DishForm only has the fields "name" and "description"
            # Before we can create the dish we have to collate more
            # information
            dish_data = {
                "default_price": dish_request_form_data["price"],
                "serving_size": dish_request_form_data["portion_size"],
                "latitude": diner.latitude,
                "longitude": diner.longitude
            }
            dish_data.update(dish_form.cleaned_data)
            dish = Dish.objects.create(**dish_data)

            # Create the DishRequest
            # Similarly, collate data not contained
            # in the validated DishRequestForm.
            dish_request_data = {
                "diner": diner,
                "dish": dish,
                "latitude": diner.latitude,
                "longitude": diner.longitude
            }
            dish_request_data.update(dish_request_form_data)
            dish_request = DishRequest.objects.create(**dish_request_data)

            return redirect("orders_and_requests")
    else:
        dish_request_form = DishRequestForm(prefix="dish_request")
        dish_form = DishForm(prefix="dish")
    context["dish_request_form"] = dish_request_form
    context["dish_form"] = dish_form
    return render(request, "dishes/create_request.html", context)

def edit_request(request, dish_request_id):
    context = {}
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    dish = dish_request.dish
    if request.method == "POST":
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            data=request.POST,
                                            instance=dish_request)
        dish_form = DishForm(prefix="dish", data=request.POST, instance=dish)
        if dish_request_form.is_valid() and dish_form.is_valid():
            dish_request_form.save()
            dish_form.save()
            return redirect("orders_and_requests")
    else:
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            instance=dish_request)
        dish_form = DishForm(prefix="dish", instance=dish_request.dish)
    context["dish_request_form"] = dish_request_form
    context["dish_form"] = dish_form
    return render(request, "dishes/edit_request.html", context)

def cancel_request(request, dish_request_id):
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    if request.method == "POST":
        dish_request.status = DishRequest.CANCELLED
        dish_request.save()
        return redirect("orders_and_requests")
    context = {"request": dish_request}
    return render(request, "dishes/cancel_request.html", context)

def create_post(request):
    context = {}
    if request.method == "POST":
        dish_post_form = DishPostForm(prefix="dish_post",
                                      data=request.POST)
        dish_form = DishForm(prefix="dish", data=request.POST)
        if dish_post_form.is_valid() and dish_form.is_valid():
            # Bind some more programmer friendly references
            diner = request.user.diner
            chef = request.user.chef
            dish_post_form_data = dish_post_form.cleaned_data

            # Create the Dish
            # The DishForm only has the fields "name" and "description"
            # Before we can create the dish we have to collate more
            # information
            dish_data = {
                "default_price": dish_post_form_data["price"],
                "serving_size": dish_post_form_data["serving_size"],
            }
            dish_data.update(dish_form.cleaned_data)
            dish = Dish.objects.create(**dish_data)

            # Create the DishPost
            # Similarly, collate data not contained
            # in the validated DishRequestForm.
            dish_post_data = {
                "chef": chef,
                "dish": dish,
                "latitude": diner.latitude,
                "longitude": diner.longitude
            }
            dish_post_data.update(**dish_post_form_data)
            dish_post = DishPost.objects.create(**dish_post_data)

            return redirect("orders_and_requests")
    else:
        dish_post_form = DishPostForm(prefix="dish_post")
        dish_form = DishForm(prefix="dish")

    context["dish_post_form"] = dish_post_form
    context["dish_form"] = dish_form
    return render(request, "dishes/create_post.html", context)

def manage_posts(request):
    chef = request.user.chef
    dish_posts = chef.dishpost_set.filter(status=DishPost.OPEN)
    context = {"dish_posts": dish_posts}
    return render(request, "dishes/manage_posts.html", context)

def cancel_post(request, dish_post_id):
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    if request.method == "POST":
        dish_post.status = DishPost.CANCELLED
        dish_post.save()
        return redirect("manage_posts")
    context = {"dish_post": dish_post}
    return render(request, "dishes/cancel_post.html", context)

def edit_post(request, dish_post_id):
    context = {}
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    dish = dish_post.dish
    if request.method == "POST":
        dish_post_form = DishPostForm(prefix="dish_post",
                                      data=request.POST,
                                      instance=dish_post)
        dish_form = DishForm(prefix="dish", data=request.POST, instance=dish)
        if dish_post_form.is_valid() and dish_form.is_valid():
            dish_post_form.save()
            dish_form.save()
            return redirect("manage_posts")
    else:
        dish_post_form = DishPostForm(prefix="dish_post", instance=dish_post)
        dish_form = DishForm(prefix="dish", instance=dish)
    context["dish_post_form"] = dish_post_form
    context["dish_form"] = dish_form
    return render(request, "dishes/edit_post.html", context)

def follow_chef(request, chef_id):
    context = {}
    chef = get_object_or_404(Chef, pk=chef_id)
    chef.userprofile.follows.add(request.user.username)
    context["Following"] = True
    return render(request, "dishes/chef_detail.html", context)

def rate_diner(request, diner_id):
    diner = get_object_or_404(Diner, pk=diner_id)
    if request.method == "POST":
        form = RateDinerForm(request.POST)
        if form.is_valid():
            int_rating = request.POST["rating"]
            rating = RateDiner.objectscreate(diner, rating=int_rating)
        else:
            form = RateDinerForm()
    return redirect(request,"dishes/rate_diner.html")

def edit_chef(request, chef_id):
    context = {}
    chef = get_object_or_404(Chef, pk=chef_id)
    if request.method == "POST":
        chef_form = ChefForm(data=request.POST, instance=chef)
        if chef_form.is_valid():
            chef_form.save()
            return redirect("chef_detail", chef_id=chef_id)
    else:
        chef_form = ChefForm(instance=chef)
    context["chef_form"] = chef_form
    return render(request, "dishes/edit_chef.html", context)

