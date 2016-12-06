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
    0: {
        "user": 0,
        "latitude": decimal.Decimal(41.019751),
        "longitude": decimal.Decimal(-73.616714)
    },
    1: {
        "user": 1,
        "latitude": decimal.Decimal(40.991531),
        "longitude": decimal.Decimal(-73.670672)
    }
}

chefs = {
    0: {
        "user": 1,
        "name": "Mark Twain",
        "blurb": "Satirist in the prosaic and culinary arts.",
        "experience": "Frying bacon and scrambling eggs. Caveat emptor."
    }
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
    },
    7: {
        "name": "Tuna Salad",
        "default_price": decimal.Decimal(5.00),
        "description": "Fresh Tuna with lettuce, onions and other healthy things",
        "serving_size": decimal.Decimal(1.0)
    },
    8: {
        "name": "Cheeseburgers",
        "default_price": decimal.Decimal(4.00),
        "description": "Burgers fresh off the grill",
        "serving_size": decimal.Decimal(10.0)
    },
    9: {
        "name": "Pizza",
        "default_price": decimal.Decimal(2.00),
        "description": "Homemade pizza with homemade sauce and cheese",
        "serving_size": decimal.Decimal(8.0)
    },
    10: {
        "name": "Biryani",
        "default_price": decimal.Decimal(8.00),
        "description": "Great tasting basmati rice and chicken cooked the Pakistani way",
        "serving_size": decimal.Decimal(2.0)
    },
    11: {
        "name": "Mango Lassi",
        "default_price": decimal.Decimal(3.00),
        "description": "Indian yogurt beverage, its got lots of different flavors<br>people like to drink it on a hot summer's day",
        "serving_size": decimal.Decimal(8.0)
    },
    12: {
        "name": "Tandoori Chicken",
        "default_price": decimal.Decimal(4.00),
        "description": "Spicy chicken seasoned with traditional Indian spices",
        "serving_size": decimal.Decimal(5.0)
    },
    13: {
        "name": "Vegetable Samosas",
        "default_price": decimal.Decimal(1.50),
        "description": "Potatoes, chickpeas, and onions wrapped inside a bread and fried",
        "serving_size": decimal.Decimal(10.0)
    },
    14: {
        "name": "Chicken Makhni",
        "default_price": decimal.Decimal(3.00),
        "description": "Chicken cooked in butter and cream, also known as Butter Chicken",
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
        "longitude": decimal.Decimal(-73.96078),
        "status": DishPost.COMPLETE
    },
    1: {
        "chef": 0,
        "max_servings": 4,
        "dish": 1,
        "price": decimal.Decimal(5.00),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() - datetime.timedelta(days=4),
        "meal_time": timezone.now() - datetime.timedelta(days=3),
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
        "dish": 3,
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
        "latitude": decimal.Decimal(40.963703),
        "longitude": decimal.Decimal(-73.858758)
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
        "latitude": decimal.Decimal(40.6450574),
        "longitude": decimal.Decimal(-73.9999147)
    },
    12: {
        "chef": 0,
        "max_servings": 6,
        "dish": 2,
        "price": decimal.Decimal(5.43),
        "serving_size": decimal.Decimal(1),
        "last_call": timezone.now() + datetime.timedelta(days=3),
        "meal_time": timezone.now() + datetime.timedelta(days=4),
        "latitude": decimal.Decimal(40.8505949),
        "longitude": decimal.Decimal(-73.8791922)
    }
}

orders = {
    0: {
        "diner": 0,
        "dish_post": 0,
        "num_servings": 1
    },
    1: {
        "diner": 0,
        "dish_post": 4,
        "num_servings": 2,
        "status": Order.PENDING_FEEDBACK
    },
    2: {
        "diner": 0,
        "dish_post": 12,
        "num_servings": 1,
        "status": Order.PENDING_FEEDBACK
    },
    3: {
        "diner": 0,
        "dish_post": 11,
        "num_servings": 2,
        "status": Order.PENDING_FEEDBACK
    },
    4: {
        "diner": 0,
        "dish_post": 10,
        "num_servings": 1,
        "status": Order.PENDING_FEEDBACK
    }
}

dish_requests = {
    0: {
        "diner": 0,
        "dish": 11,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.6675515),
        "longitude": decimal.Decimal(-73.9869256)
    },
    1: {
        "diner": 0,
        "dish": 9,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.7486386),
        "longitude": decimal.Decimal(-73.895272)
    },
    2: {
        "diner": 0,
        "dish": 10,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.6486386),
        "longitude": decimal.Decimal(-73.87915727)
    },
    3: {
        "diner": 0,
        "dish": 12,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.8505949),
        "longitude": decimal.Decimal(-73.8791922)
    },
    4: {
        "diner": 0,
        "dish": 13,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.7483135),
        "longitude": decimal.Decimal(-73.8851868)
    },
    5: {
        "diner": 0,
        "dish": 14,
        "portion_size": decimal.Decimal(1.1),
        "num_servings": 5,
        "price": decimal.Decimal(6.50),
        "meal_time": timezone.now() + datetime.timedelta(days=7),
        "latitude": decimal.Decimal(40.7523781),
        "longitude": decimal.Decimal(-73.9200795)
    },
    

}

red_flags = {
    0: { "user": 0, "reason": 0 }
}

complaints = {
    0: {
        "complainant": 0,
        "complainee": 1,
        "order": 0,
        "description": "She smiled at me too warmly."
    }
}

create_account_requests = {
    0: {
        "username": "mm34",
        "first_name": "winnie",
        "last_name": "poo",
        "email": "walt@disney.com"
    },
    1: {
        "username": "kib210",
        "first_name": "most",
        "last_name": "least",
        "email": "sig@byte.com"
    }
}

suspension_info = {
    0: {"user": 0},
    1: {"user": 1}
}

def load():

    for user_info in users:
        user = User(username=users[user_info]["username"],
                    email=users[user_info]["email"])
        user.set_password(users[user_info]["password"])
        users[user_info] = user
        user.save()

    for key in diners:
        diners[key]["user"] = users[diners[key]["user"]]
        diner = Diner.objects.create(**diners[key])
        diners[key] = diner

    for chef_info in chefs:
        chefs[chef_info]["user"] = users[chefs[chef_info]["user"]]
        chef = Chef.objects.create(**chefs[chef_info])
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

    for key in complaints:
        complaints[key]["complainant"] = users[complaints[key]["complainant"]]
        complaints[key]["complainee"] = users[complaints[key]["complainee"]]
        complaints[key]["order"] = orders[complaints[key]["order"]]
        complaint = Complaint.objects.create(**complaints[key])
        complaints[key] = complaint

    for key in create_account_requests:
        create_account_request = CreateAccountRequest.objects.create(
                                    **create_account_requests[key]
                                )
        create_account_requests[key] = create_account_request

    for key in suspension_info:
        suspension_info[key]["user"] = users[suspension_info[key]["user"]]
        suspension_count = SuspensionInfo.objects.create(**suspension_info[key])
        suspension_info[key] = suspension_count


    User.objects.create_superuser("admin",
                                  "admin@example.com",
                                  "uncommonpassword")

def delete():

    models = [
        User,
        Diner,
        Chef,
        CuisineTag,
        Order,
        DishPost,
        DishRequest,
        Dish,
        RedFlag,
        Complaint,
        CreateAccountRequest,
        SuspensionInfo
    ]

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
