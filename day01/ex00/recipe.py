import operator

class Recipe:

	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	name = property(operator.attrgetter("_name"))
	@name.setter
	def name(self, v):
		if type(v) is not str:
			raise TypeError("Name should be a string moron !")
		if not v:
			raise ValueError("Name can't be null")
		self._name = v

	cooking_lvl = property(operator.attrgetter("_cooking_lvl"))
	@cooking_lvl.setter
	def cooking_lvl(self, v):
		if v < 1 or v > 5:
			raise ValueError("Cooking_lvl can only be from 1 to 5 included")
		self._cooking_lvl = v

	cooking_time = property(operator.attrgetter("_cooking_time"))
	@cooking_time.setter
	def cooking_time(self, v):
		if v < 0:
			raise ValueError("Cooking_time can't be negative")
		self._cooking_time = v

	ingredients = property(operator.attrgetter("_ingredients"))
	@ingredients.setter
	def ingredients(self, v):
		if type(v) is not list or not all(isinstance(c, str) for c in v):
			raise TypeError("Ingredients should be a list of str !!")
		if len(v) < 1:
			raise ValueError("At least one ingredient...")
		if len([i for i in v if not i]):
			raise ValueError("No null ingredients... Moron !")
		self._ingredients = v

	description = property(operator.attrgetter("_description"))
	@description.setter
	def description(self, v):
		if type(v) is not str:
			raise TypeError("Description Should be a string !")
		self._description = v

	recipe_type = property(operator.attrgetter("_recipe_type"))
	@recipe_type.setter
	def recipe_type(self, v):
		if type(v) is not str:
			raise ValueError("recipe_type should be a string")
		if v != "starter" and v != "lunch" and v != "dessert":
			raise ValueError("recipe_type can only be 'starter', 'lunch' or 'dessert'")
		self._recipe_type = v

	def __str__(self):
		"""Return the string to print with the recipe info"""
		return (
			f"Recipe : {self.name}\n"
			f"Cooking level : {self.cooking_lvl}\n"
			f"Cooking time : {self.cooking_time}\n"
			f"Ingredients : {self.ingredients}\n"
			f"Description : {self.description}\n"
			f"Recipe type : {self.recipe_type}\n"
		)

	def __repr__(self):
		return ("Recipe({}, {}, {}, {}, {}, {})".format(
			self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description,	self.recipe_type
		)
		)
