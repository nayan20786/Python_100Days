# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.right(25)
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikachu","Charmander","Snorlax"])
table.add_column ("Type",["Electric","Fire","Grass"])
table.align='r'
print(table)
