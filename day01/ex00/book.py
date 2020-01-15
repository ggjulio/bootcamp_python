import datetime as dt
from typing import Type
from recipe import Recipe

class Book:
    def __init__(self, name: str):
        self.name = name
        self.creation_date = (dt.datetime.now() if Recipe.creation_date is None)
        self.last_update = dt.datetime.now()
        self.recipe_list = recipe_list

        def get_recipe_by_name(self, name):
            """Print a recipe with the name `name` and return the instance"""
            pass
        def get_recipes_by_types(self, recipe_type):
            """Get all recipe names for a given recipe_type """
            pass
        def add_recipe(self, recipe):
            """Add a recipe to the book and update last_update"""
            pass

