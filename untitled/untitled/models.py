from django.db import models


# open_cart table schema
class open_cart(models.Model):
    class Meta:
        db_table = 'open_cart'
    rd_customer_tag = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200,primary_key=True)
    event_time_ts = models.DecimalField(decimal_places=15,max_digits=28)
    order_id = models.DecimalField(decimal_places=15,max_digits=28)
    date_added = models.DecimalField(decimal_places=15,max_digits=28)
    order_status = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    order_total = models.DecimalField(decimal_places=15,max_digits=28)
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(decimal_places=15,max_digits=28)
    payment_country = models.CharField(max_length=200)
    payment_city = models.CharField(max_length=50)
    payment_zone = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=200)
    shipping_country = models.CharField(max_length=200)
    shipping_zone = models.CharField(max_length=100)
    shipping_method = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(decimal_places=15,max_digits=28)
    category_name = models.CharField(max_length=200)
    option_name = models.CharField(max_length=50)
    option_value = models.CharField(max_length=50)


# open_cart_filtered table schema
class open_cart_filtered(models.Model):

    rd_customer_tag = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    event_time_ts = models.DecimalField(decimal_places=15,max_digits=28)
    order_id = models.DecimalField(decimal_places=15,max_digits=28)
    date_added = models.DecimalField(decimal_places=15,max_digits=28)
    order_status = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    order_total = models.DecimalField(decimal_places=15,max_digits=28)
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(decimal_places=15,max_digits=28)
    payment_country = models.CharField(max_length=200)
    payment_city = models.CharField(max_length=50)
    payment_zone = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=200)
    shipping_country = models.CharField(max_length=200)
    shipping_zone = models.CharField(max_length=100)
    shipping_method = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    prodcut_price = models.DecimalField(decimal_places=15,max_digits=28)
    category_name = models.CharField(max_length=200)
    option_name = models.CharField(max_length=50)
    option_value = models.CharField(max_length=50)
