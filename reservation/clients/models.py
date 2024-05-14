from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100, help_text="Type of client (e.g., Individual, Company)")

    def __str__(self):
        return self.name
class Client(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the client")
    address = models.TextField(help_text="Address of the client")
    phone = models.CharField(max_length=15, blank=True, help_text="Contact phone number")
    email = models.EmailField(blank=True, help_text="Email address")
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, help_text="Type of client")

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the product")
    description = models.TextField(blank=True, help_text="Description of the product")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price of the product")

    def __str__(self):
        return self.name
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, help_text="Client who placed the order")
    order_date = models.DateField(auto_now_add=True, help_text="Date the order was placed")
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, help_text="Total amount of the order")

    def __str__(self):
        return f"Order {self.id} - {self.client.name}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE, help_text="Order associated with the product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Product ordered")
    quantity = models.IntegerField(help_text="Quantity of the product ordered")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price at the time of order")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order {self.order.id}"
