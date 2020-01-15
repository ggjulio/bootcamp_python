from book import Book 
from recipe import Recipe

my_book = Book("Yes")
a = Recipe(name="Sans Gluten", cooking_lvl=1, cooking_time=1000,ingredients=["Trop","de", "legumes"], description="Indescriptible", recipe_type="lunch")
b = Recipe(name="pizza cannibale", cooking_lvl=1, cooking_time=15,ingredients=["boeuf","poulet", "mergez", "fromage", "sauce tomate"], description="excellent !", recipe_type="lunch")
c = Recipe(name="pates gruyere", cooking_lvl=5, cooking_time=10,ingredients=["pates","gruyere"], description="la base", recipe_type="lunch")
d = Recipe(name="Burger nutella", cooking_lvl=1, cooking_time=2,ingredients=["Pain burger","Nutella"], description="Nop", recipe_type="dessert")
e = Recipe(name="Burger nutella", cooking_lvl=1, cooking_time=2,ingredients=["Pain burger","Nutella"], description="Nop", recipe_type="dessert")

my_book.add_recipe(a)
my_book.add_recipe(b)
my_book.add_recipe(c)
my_book.add_recipe(d)


