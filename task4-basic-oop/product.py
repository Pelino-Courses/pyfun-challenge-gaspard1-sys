class Product:
    """
    attributes:
    name(str):name of product
    price(foat): amount for each product
    quantity(int):the number of product in stock

    """
    def __init__(self,name:str, price:float, quantity:int):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price per unit (must be non-negative).
            quantity (int): The quantity in stock (must be non-negative).

        Raises:
            ValueError: If price or quantity is negative.

        """
        if price < 0:
            raise ValueError("Price must be pasitive.")
        if quantity < 0:
            raise ValueError("Quantity must be positive.")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount: int):
        """
        fuction add_inventory has this args
        Args:
            amount (int): The amount to add (must be positive).

        Raises:
            ValueError: If amount lessthan zero.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative amount to inventory.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
         if amount < 0:
            raise ValueError("Cannot remove a negative amount from inventory.")
         if amount > self.quantity:
            raise ValueError("Cannot remove more than available inventory.")
         self.quantity -= amount

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of the current inventory.

        Returns:
            float: The total value (price * quantity).
        """
        return self.price * self.quantity

    def display_product_info(self):
        """
        Displays detailed product information.
        """
        print(f"Product Name: {self.name}")
        print(f"Price per Unit: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Total Inventory Value: ${self.calculate_total_value():.2f}")
obj = Product("book", 18000.965, 100)
obj.display_product_info()
obj.remove_inventory(3)
obj.display_product_info()
obj.remove_inventory(1)








