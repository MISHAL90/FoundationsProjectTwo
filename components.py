# CLASSES AND METHODS
class Store():
	def __init__(self, name):
		"""
		Initializes a new store with a name.
		"""
		# your code goes here!
		self.products = []
		self.name = name



	def add_product(self, product):
		"""
		Adds a product to the list of products in this store.
		"""
		# your code goes here!
		self.products.append(product)

	def print_products(self):
		"""
		Prints all the products of this store in a nice readable format.
		"""
		# your code goes here!
		for item in self.products:
			print(item)


class Product():
	def __init__(self, name, description, price):
		"""
		Initializes a new product with a name, a description, and a price.
		"""
		# your code goes here!
		self.name = name    
		self.description = description
		self.price = price

	def __str__(self):
		# your code goes here!
		return("(%s, %s, %s)" % (self.name, self.description, self.price))



class Cart():
	def __init__(self):
		"""
		Initializes a new cart with an empty list of products.
		"""
		# your code goes here
		self.cart = []

	def add_to_cart(self, product):
		"""
		Adds a product to this cart.
		"""
		# your code goes here!
		self.cart.append(product)

	def get_total_price(self):
		"""
		Returns the total price of all the products in this cart.
		"""
		# your code goes here!
		total=0
		for product in self.cart:
			total+=product.price
		return total    

	def print_receipt(self):
		"""
		Prints the receipt in a nice readable format.
		"""
		# your code goes here!
		for product in self.cart:
			print( product )
		(print ("Your Total Is %s" % self.get_total_price() ))

	def checkout(self):
		"""
		Does the checkout.
		"""
		# your code goes here!
		self.print_receipt()
		user_input= input (" Do you confirm (y/n)? ").lower()
		if user_input == "y":
			print (" Your order is confirm")
		elif user_input=="n":
			ptint (" your oder is cancel")
		else:
			print("wrong input")
			self.checkout()