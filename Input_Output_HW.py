import math
#8 slices
#family of 4
#calculate the numbers of whole pizzas
#how many leftover slices

Pizza_eaten= int(input('How many slices did everyone eat '))

Family=4

whole_pizza= 8

Pizza_eaten_together= (Family * Pizza_eaten)

Amount_of_pizza_needed= math.ceil(Pizza_eaten_together/whole_pizza)

print('This is amount of whole pizza needed',Amount_of_pizza_needed )

#leftovers

Amount_pizza_left=Pizza_eaten_together%whole_pizza

print('leftovers are',Amount_pizza_left) 

