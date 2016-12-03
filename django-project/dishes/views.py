from django.shortcuts import get_object_or_404, render, redirect
from dishes.models import DishPost, Diner, Order, DishRequest, Chef, OrderFeedback, RateChef
from dishes.forms import DishForm, DishRequestForm, DishPostForm, FeedbackForm, RateChefForm


def posts(request):
    dish_posts = DishPost.objects.all()
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
        diner = Diner.objects.get(user=request.user)
        orders = Order.objects.filter(diner=diner)
        requests = DishRequest.objects.filter(diner=diner)
        is_chef = hasattr(request.user, "chef")
        context = {
            "orders": orders,
            "requests": requests,
            "is_chef": is_chef
        }
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

def chef_bio(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    context = {"chef": chef}
    return render(request, "dishes/chef_bio.html", context)

def rate_chef(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    if request.method == "POST":
        form = RateChefForm(request.POST)
        if form.is_valid():
            int_rating = request.POST["rating"]
            rating = RateChef.objects.create(chef,rating=int_rating)
        else:
            form = RateChefForm()
    return redirect("chef_detail")

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

def edit_request(request, dish_request_id):
    context = {}
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    if request.method == "POST":
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            data=request.POST)
        dish_form = DishForm(prefix="dish", data=request.POST)
        if dish_request_form.is_valid() and dish_form.is_valid():
            # Update the Dish and DishRequest
            return redirect("orders_and_requests")
    else:
        dish_request_form = DishRequestForm(prefix="dish_request",
                                            instance=dish_request)
        dish_form = DishForm(prefix="dish", instance=dish_request.dish)
    context["dish_request_form"] = dish_request_form
    context["dish_form"] = dish_form
    return render(request, "dishes/edit_request.html", context)

def cancel_request(request, dish_request_id):
    if request.method == "POST":
        return redirect("orders_and_requests")
    dish_request = get_object_or_404(DishRequest, pk=dish_request_id)
    context = {"request": dish_request}
    return render(request, "dishes/cancel_request.html", context)

def create_post(request):
    context = {}
    import pdb; pdb.set_trace()
    if request.method == "POST":
        dish_post_form = DishPostForm(prefix="dish_post",
                                      data=request.POST)
        dish_form = DishForm(prefix="dish", data=request.POST)
        if dish_post_form.is_valid() and dish_form.is_valid():
            # Create the Dish and DishPost
            return redirect("orders_and_requests")
    else:
        dish_post_form = DishPostForm(prefix="dish_post")
        dish_form = DishForm(prefix="dish")
    context["dish_post_form"] = dish_post_form
    context["dish_form"] = dish_form
    return render(request, "dishes/create_post.html", context)

def manage_posts(request):
    dish_posts = DishPost.objects.filter(chef=request.user.chef)
    context = {"dish_posts": dish_posts}
    return render(request, "dishes/manage_posts.html", context)

def cancel_post(request, dish_post_id):
    if request.method == "POST":
        return redirect("manage_posts")
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    context = {"dish_post": dish_post}
    return render(request, "dishes/cancel_post.html", context)

def edit_post(request, dish_post_id):
    context = {}
    dish_post = get_object_or_404(DishPost, pk=dish_post_id)
    dish = dish_post.dish
    if request.method == "POST":
        dish_post_form = DishPostForm(prefix="dish_post",
                                      data=request.POST)
        dish_form = DishForm(prefix="dish", data=request.POST)
        if dish_post_form.is_valid() and dish_form.is_valid():
            # Update the Dish and DishPost
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
    chef.userprofile.followers.add(request.user.username)
    context["Following"] = True
    return render(request, "dishes/chef_detail.html", context)

