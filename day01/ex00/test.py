from book import Book 
from recipe import Recipe

my_book = Book("Yes")
a = Recipe(name="Sans Gluten", cooking_lvl=5, cooking_time=1000,ingredients=["Trop","de", "legumes"], description="Indescriptible", recipe_type="lunch")

my_book.add_recipe(a)

