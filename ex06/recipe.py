
cookbook = {
"sandwich" : {
		"incredients" : {"flour", "sugar", "eggs"},
		"meal" :"dessert",
		"prep_time" : 60
		},
"cake" : {
		"incredients" : {"flour", "sugar", "eggs"},
		"meal" :"dessert",
		"prep_time" : 60		
		},
"salad" : {
		"incredients" : {"flour", "sugar", "eggs"},
		"meal" :"dessert",
		"prep_time" : 60
		}
}

#def add_recipe():
    
#def delete_recipe():
	
#def print_recipe():

#def print_cookbook():
    
n = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ")
while 1:
	try:
		n = int(n);
	except ValueError:
		continue
	if n < 0 and n > 5:
		n = input("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n>> ")


