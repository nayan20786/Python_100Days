# Day6 Functions

# Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
#
# Reeborg Hurdle1 Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# for a in range(6):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# While loop Hurdle 3 Solution:
# while not at_goal():
#     while front_is_clear() and not at_goal():
#         move()
#
#     if not front_is_clear():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()

# Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

exit()


# Sample functions
def calculateFun(a):
    return 2 * a


b = calculateFun(2)
print(b)
