import os
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 40
MAP_HEIGHT = 35

my_position = [3, 1]
tail_length = 0
tail = []
map_objects = [[2, 3], [5, 4], [3, 4], [10, 6]]


def displayGame():
    os.system("clear")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):

        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"

            for i in range(tail_length):
                if tail[i] == [coordinate_x, coordinate_y]:
                    char_to_draw = "@"

            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
            delete_objects()

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("Score: {}".format(tail_length))
    print("Press 'q' to quit")


def delete_objects():
    global tail_length
    for map_object in map_objects:
        if map_object[POS_X] == my_position[POS_X] and map_object[POS_Y] == my_position[POS_Y]:
            tail_length += 1
            map_objects.remove(map_object)
            if map_objects == []:
                generate_random_objects()


def generate_random_objects():
    for i in range(10):
        random_x = random.randint(0, MAP_WIDTH - 1)
        random_y = random.randint(0, MAP_HEIGHT - 1)
        map_objects.append([random_x, random_y])


while True:

    displayGame()

    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        if((my_position[POS_Y] - 1) <= -1):
            my_position[POS_Y] = MAP_HEIGHT - 1
        else:
            my_position[POS_Y] -= 1
    elif direction == "a":
        tail.insert(0, my_position.copy())
        if(my_position[POS_X] - 1 <= -1):
            my_position[POS_X] = MAP_WIDTH - 1
        else:
            my_position[POS_X] -= 1
    elif direction == "s":
        tail.insert(0, my_position.copy())
        if(my_position[POS_Y] + 1 >= MAP_HEIGHT):
            my_position[POS_Y] = 0
        else:
            my_position[POS_Y] += 1
    elif direction == "d":
        tail.insert(0, my_position.copy())
        if(my_position[POS_X] + 1 >= MAP_WIDTH):
            my_position[POS_X] = 0
        else:
            my_position[POS_X] += 1
    elif direction == "q":
        break
    else:
        print("invalid key")

    displayGame()
