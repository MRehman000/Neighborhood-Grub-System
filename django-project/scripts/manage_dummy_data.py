import os
import sys
import decimal
import datetime
import argparse

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "ngs.settings"
ngs_dir, gbg = os.path.split(os.path.abspath(__file__))
ngs_dir, gbg = os.path.split(ngs_dir)
sys.path.append(ngs_dir)
django.setup()

from django.contrib.auth.models import User

from dishes.models import *

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
        "default_price": decimal.Decimal(7.50),
        "description": "Sesame Chicken",
        "serving_size": 5
    }
}

dish_posts = {
    0: {
        "chef": 0,
        "max_servings": 3,
        "dish": 0,
        "price": decimal.Decimal(6.50),
        "serving_size": decimal.Decimal(0.7),
        "last_call": datetime.datetime.now() + datetime.timedelta(days=1),
        "meal_time": datetime.datetime.now() + datetime.timedelta(days=2)
    }
}

orders = {
    0: {
        "diner": 0,
        "dish_post": 0,
        "num_servings": 1
    }
}

def load():

    for user_info in users:
        user = User.objects.create(**users[user_info])
        user.set_password(users[user_info]["password"])
        users[user_info] = user

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

def delete():

    models = [User, Diner, Chef, CuisineTag, Order, DishPost, Dish]
    for model in models:
        model.objects.all().delete()

def main(command):

    print(command)
    if command == "load":
        load()
    elif command == "delete":
        delete()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="load or delete")
    args = parser.parse_args()
    main(args.command)
