import operator
import datetime as dt
from recipe import Recipe

class Book:
	def __init__(self, name: str):
		self.name = name
		self.creation_date = dt.datetime.now()
		self.last_update = self.creation_date
		self.recipe_dict = {
							"starter" : [],
							"lunch" : [], 
							"dessert" : []
							}

	name = property(operator.attrgetter("_name"))
	@name.setter
	def name(self, v):
		if type(v) is not str:
			raise TypeError("Name should be a string moron !")
		if not v:
			raise ValueError("Name can't be null")
		self._name = v

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for recipe in sum(self.recipe_dict.values(), []):
			if recipe.name == name:
				print(str(recipe))
				return(recipe)

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		return (self.recipe_dict[recipe_type])

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if type(recipe)is not Recipe:
			raise TypeError("This is NOT a recipe !")
		if recipe.name in [r.name for r in self.recipe_dict[recipe.recipe_type]]:
			raise ValueError(f"NO ! Recipe {recipe.name} already exist !")
		self.recipe_dict[recipe.recipe_type].append(recipe)
		self.last_update = dt.datetime.now()

