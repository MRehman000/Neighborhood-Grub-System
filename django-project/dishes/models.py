from django.db import models
from django.contrib.auth.models import User

class Diner(models.Model):
    """
    Django model class representing a Diner.

    Attributes:

    user:
        The User account associated with this Diner instance.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Chef(models.Model):
    """
    Django model class representing a Chef.

    Attributes:

    user:
        The User account associated with this Chef instance.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CuisineTag(models.Model):
    """
    Django model class representing a cuisine tag.
    """
    name = models.CharField(max_length=64, unique=True)

class Dish(models.Model):
    """
    Django model class representing a dish in NGS.
    """

    """ The default price of the dish.

    Since the same Dish instance may be used to create multiple Dish Requests
    and Dish Posts we must decouple the price information from the template.
    Otherwise one could not change the price of one Request without changing
    all the others. Also, price history information would also need to be
    preserved separately.

    max_digits=4 and decimal_places=2 limits the price to no more than $99.99.
    """
    default_price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField("Dish Description")
    cuisine_tags = models.ManyToManyField(CuisineTag)
    serving_size = models.DecimalField(max_digits=3,
                                       decimal_places=1,
                                       default=4.99)

class DishPost(models.Model):
    """
    Django model class representing a Dish posted by a Chef for a Diner to
    order.

    Attributes:

    chef:
        Foreign Key field referencing the Chef who has created this Dish
        Post.

    diners:
        Many to Many field mapping DishPosts to Diners.

    dish:
        Foreign key field referencing the Dish the Chef is going to cook.

    price:
        Decimal field that stores the price of one serving of this Dish.

    max_servings:
        Integer field that indicates the maximum servings of this Dish the Chef
        is willing to cook.

    serving_size:
        Decimal field that indicates the size of one serving in NGS containers.

    last_call:
        Date time field that indicates the time past which the Chef will not
        accept further orders.

    meal_time:
        Date time field that indicates the approximate time the Dish is to be
        served. The Chef and Diner should coordinate the exchange of food at or
        around this time.

    status:
        Integer field that indicates the status of the order. The status
        descriptions are below.

        Open:
            At least 1 serving of the Dish Post is still available so a Diner
            may still order the Dish.
        Closed:
            The Dish has not yet been served, but is not availalbe for further
            orders. This may be because the maximum number of orders has been
            reached, or the Dish is past the order point.
        Cancelled:
            The Chef has cancelled this Dish Post.
        Complete:
            The Dish has been served and the Chef has been paid.
    """
    chef = models.ForeignKey(Chef, on_delete=models.SET_NULL, null=True)
    max_servings = models.IntegerField(default=1)
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    serving_size = models.DecimalField(max_digits=3, decimal_places=1)
    last_call = models.DateTimeField("Last Call")
    meal_time = models.DateTimeField("Meal Time")

    OPEN = 0
    CLOSED = 1
    CANCELLED = 2
    COMPLETE = 3

    STATUS_CHOICES = (
        (OPEN, "Open"),
        (CLOSED, "Closed"),
        (CANCELLED, "Cancelled"),
        (COMPLETE, "Complete")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=OPEN)

class Order(models.Model):
    """
    Django model class representing an Order made by a Diner for a Posted Dish.
    The Order model is used to capture the mapping of Diners to Dish Posts
    and how many servings of the of the Dish Post the Diner wishes to have.

    Attributes:

    diner:
        The Diner placing the order.

    dish_post:
        The Dish Post the diner is ordering.

    num_servings:
        The number of servings of the Dish the Diner wishes to order.
    """
    diner = models.ForeignKey(Diner, on_delete=models.SET_NULL, null=True)
    dish_post = models.ForeignKey(DishPost, on_delete=models.PROTECT)
    num_servings = models.IntegerField(default=1)
