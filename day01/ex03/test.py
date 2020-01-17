from generator import generator 

text = "Le Lorem Ipsum est simplement du faux texte."


for word in generator(text, sep=" "):
	print(word)

print ("\n\n\n")
for word in generator(text, sep=" ", option="shuffle"):
	print(word)

print ("\n\n\n")

for word in generator(text, sep=" ", option="ordered"):
	print(word)

print ("\n\n\n")

for word in generator(text, sep=" ", option=None):
	print(word)