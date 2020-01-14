import operator

class Recipe:

#    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    def __init__(self, name: str):
        self.name = name
#        self.cooking_lvl = cooking_lvl
#        self.cooking_time = cooking_time
#        self.ingredients = ingredients
#        self.description = description
#        self.recipe_type = recipe_type

    name = property(operator.attrgetter('_name'))
    @name.setter
    def name(self, n):
        if type(n) is not str:
            raise Exception("Name should be a string")
        self._name = n


#    @property
#    def cooking_time(self):
#        return self._cooking_time
#
#    @cooking_time.setter
#    def cooking_time(self, c):
#        if (c < 0):
#            raise Exception("Cooking_time can't be negative")
#        self._cooking_time = c
#
#
#    cooking_lvl = property(operator.attrgetter('_cooking_lvl'))
#
#    @cooking_lvl.setter
#    def cooking_lvl(self, c):
##            if cooking_lvl < 1 or cooking_lvl > 5:
#        if 1:
#            raise Exception("Cooking_lvl can only be from 1 to 5 included")
#        self._cooking_time = c
#
#            
#        
#    def __str__(self):
#        """Return the string to print with the recipe info"""
#        txt = ""
#        return txt
#
#