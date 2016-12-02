import os
import sys
import decimal
import datetime
import argparse

import django
from django.utils import timezone

os.environ["DJANGO_SETTINGS_MODULE"] = "ngs.settings"
ngs_dir, gbg = os.path.split(os.path.abspath(__file__))
ngs_dir, gbg = os.path.split(ngs_dir)
sys.path.append(ngs_dir)
django.setup()

from django.contrib.auth.models import User

from dishes.models import *
from accounts.models import *

users = {
    0: {
        "username": "foo",
        "email": "foo@bar.com",
        "password": "foopass"
    },
    1: {
        "username": "chef_one",
        "email": "best@chef.com",
        "password": "gordonramsey"
    }
}

diners = {
    0: {"user": 0},
    1: {"user": 1}
}

chefs = {
    0: {"user": 1}
}

cuisine_tags = {
    0: "Chinese",
    1: "Italian",
    2: "Indian"
}

dishes = {
    0: {
        "name": "Sesame Chicken",
        "default_price": decimal.Decimal(7.50),
        "description": ("Classic sesame chicken with white rice and choice "
                        "of sauce. More MSG than is legal!!!"),
        "serving_size": decimal.Decimal(1.5)
    },
    1: {
        "name": "Rice and Beans",
        "default_price": decimal.Decimal(5.75),
        "description": ("Does rice and beans need a description? "
                        "Of course not!"),
        "serving_size": decimal.Decimal(1)
    },
    2: {
        "name": "Beef with Broccoli",
        "default_price": decimal.Decimal(6.75),
        "description": "Masscared cow and harvested greens",
        "serving_size": decimal.Decimal(1.0)
    },

    3: {
        "name": "Halal Chicken Over Rice",
        "default_price": decimal.Decimal(6.00),
        "description": "Egyptian guy at CCNY with the best Halal!",
        "serving_size": decimal.Decimal(10.0)
    },

    4: {
        "name": "Fish and Chips",
        "default_price": decimal.Decimal(4.50),
        "description": "Fried fish served with homemade fries",
        "serving_size": decimal.Decimal(1.0)
    },

    5: {
        "name": "Fried Chicken",
        "default_price": decimal.Decimal(2.50),
        "description": "Classic fried chicken, you won't go back to KFC after eating this!",
        "serving_size": decimal.Decimal(1.0)
    },

    6: {
        "name": "Classic NY Cheesecake",
        "default_price": decimal.Decimal(3.00),
        "description": "Cheesecake NY style",
        "serving_size": decimal.Decimal(8.0)
    }
}

dish_posts = {
    0: {
        "chef": 0,
        "max_servings": 3,
        "dish": 0,
        "price": decimal.Decimal(6.50),
        "serving_size": decimal.Decimal(0.7),
        "last_call": timezone.now() + datetime.timedelta(days=1),
        "meal_time": timezone.now() + datetime.timedelta(days=2),

        "latitude": decimal.Decimal(40.8197061),
        "longitude": decimal.Decimal(-73.96078)
    },
    1: {
        "chef": 0,
        "max_servings": 4,
        "dish": 1,
        "price": decimal.Decimal(5.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197061),
        "longitude": decimal.Decimal(-73.9505599)
    },

    2: {
        "chef": 0,
        "max_servings": 10,
        "dish": 2,
        "price": decimal.Decimal(10.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.7197061),
        "longitude": decimal.Decimal(-73.9505599)
    },
    3: {
        "chef": 0,
        "max_servings": 4,
        "dish": 3,
        "price": decimal.Decimal(99.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.9197061),
        "longitude": decimal.Decimal(-73.9505599)
    },
    4: {
        "chef": 0,
        "max_servings": 4,
        "dish": 6,
        "price": decimal.Decimal(5.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197061),
        "longitude": decimal.Decimal(-73.2505599)
    },
    5: {
        "chef": 0,
        "max_servings": 4,
        "dish": 5,
        "price": decimal.Decimal(50.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(41.8197061),
        "longitude": decimal.Decimal(-73.9505599)
    },
    6: {
        "chef": 0,
        "max_servings": 4,
        "dish": 4,
        "price": decimal.Decimal(5.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197061),
        "longitude": decimal.Decimal(-72.9505599)
    },
    7: {
        "chef": 0,
        "max_servings": 4,
        "dish": 2,
        "price": decimal.Decimal(51.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197061),
        "longitude": decimal.Decimal(-74.005599)
    },
    8: {
        "chef": 0,
        "max_servings": 4,
        "dish": 1,
        "price": decimal.Decimal(8.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.2397061),
        "longitude": decimal.Decimal(-73.94059)
    },
    9: {
        "chef": 0,
        "max_servings": 6,
        "dish": 3,
        "price": decimal.Decimal(5.43),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(38.11961),
        "longitude": decimal.Decimal(-72.5505599)
    },

    10: {
        "chef": 0,
        "max_servings": 6,
        "dish": 2,
        "price": decimal.Decimal(5.43),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197031),
        "longitude": decimal.Decimal(-73.96128)
    },
    11: {
        "chef": 0,
        "max_servings": 6,
        "dish": 4,
        "price": decimal.Decimal(5.43),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.8197001),
        "longitude": decimal.Decimal(-73.938)
    },
    12: {
        "chef": 0,
        "max_servings": 6,
        "dish": 2,
        "price": decimal.Decimal(5.43),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),

        "latitude": decimal.Decimal(40.87009),
        "longitude": decimal.Decimal(-73.96021)
    }
}

orders = {
    0: {
        "diner": 0,
        "dish_post": 0,
        "num_servings": 1
    }
}

dish_requests = {
    0: {
        "diner": 0,
        "dish": 2,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7)
    }
}

red_flags = {
    0: { "user": 0 }
}

def load():

    for user_info in users:
        user = User(username=users[user_info]["username"],
                    email=users[user_info]["email"])
        user.set_password(users[user_info]["password"])
        users[user_info] = user
        user.save()

    for diner_info in diners:
        diner_user = users[diners[diner_info]["user"]]
        diner = Diner.objects.create(user=diner_user)
        diners[diner_info] = diner

    for chef_info in chefs:
        chef_user = users[chefs[chef_info]["user"]]
        chef = Chef.objects.create(user=chef_user)
        chefs[chef_info] = chef

    for tag_info in cuisine_tags:
        tag = CuisineTag.objects.create(name=cuisine_tags[tag_info])
        cuisine_tags[tag_info] = tag

    for dish_info in dishes:
        dish = Dish.objects.create(**dishes[dish_info])
        dishes[dish_info] = dish

    for key in dish_posts:
        dish_posts[key]["chef"] = chefs[dish_posts[key]["chef"]]
        dish_posts[key]["dish"] = dishes[dish_posts[key]["dish"]]
        dish_post = DishPost.objects.create(**dish_posts[key])
        dish_posts[key] = dish_post

    for key in orders:
        orders[key]["diner"] = diners[orders[key]["diner"]]
        orders[key]["dish_post"] = dish_posts[orders[key]["dish_post"]]
        order = Order.objects.create(**orders[key])
        orders[key] = order

    for key in dish_requests:
        dish_requests[key]["diner"] = diners[dish_requests[key]["diner"]]
        dish_requests[key]["dish"] = dishes[dish_requests[key]["dish"]]
        dish_request = DishRequest.objects.create(**dish_requests[key])
        dish_requests[key] = dish_request

    for key in red_flags:
        red_flags[key]["user"] = users[red_flags[key]["user"]]
        red_flag = RedFlag.objects.create(**red_flags[key])
        red_flags[key] = red_flag

    User.objects.create_superuser("admin",
                                  "admin@example.com",
                                  "uncommonpassword")

def delete():

    models = [User, Diner, Chef, CuisineTag, Order, DishPost, DishRequest, Dish, RedFlag]
    for model in models:
        model.objects.all().delete()

def main(command):

    print(command)
    if command == "load":
        load()
    elif command == "delete":
        delete()
    elif command == "reload":
        delete()
        load()
    else:
        print("Please pass as argument either load, delete, or reload")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="load or delete")
    args = parser.parse_args()
    main(args.command)
