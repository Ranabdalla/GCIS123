# activity 2  Done by Rana Naren and Danay
from turtle import Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'


def initialization(turta):
    '''
    Function which sets the speed, pencolor, and the starting point of the turtle to start drawing.
    '''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)  # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

#part 1 Rana
"""This get_color(char) function helps to pair each character with a color. 
For instance if you enter '2' it will tell you 'red'. 
If the character is not in the list, it simply returns nothing"""

def get_color(char):
    color_dictonary = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    return color_dictonary.get(char)

"""This function uses turtle to draw out a square as a pixel and fills it with a color"""
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill() 

    turta.forward(PIXEL_SIZE) 
    turta.right(90)  
    turta.forward(PIXEL_SIZE) 
    turta.right(90)  
    turta.forward(PIXEL_SIZE) 
    turta.right(90) 
    turta.forward(PIXEL_SIZE) 
    turta.right(90) 
    turta.end_fill() 
    turta.penup() 
    turta.forward(PIXEL_SIZE) 
    turta.pendown() 
"""this function is to identify the color of the pixel inputed 
from the user from the color dictionary"""
def draw_pixel(color_string, turta):
    color = get_color(color_string)
    if color:
        draw_color_pixel(color, turta)
        return True
    else:
        return False
    
"""takes a string of colors and loops each character in the string
 and calls the draw_pixel function. If any pixel cannot be drawn it stops."""

def draw_line_from_string(color_string, turta):
    for char in color_string:
        if not draw_pixel(char, turta):
            return False
    return True

"""to move turtle to the start of the next row"""
def next_row(turta):
    turta.penup()
    current_x, current_y = turta.position()
    turta.goto(-PIXEL_SIZE*COLUMNS / 2, current_y - PIXEL_SIZE)    
    turta.pendown()

"""asks the user to input a string of numbers and A, 
then it calls the draw_line_from_string to draw each line based on the string. 
If there is an invalid input(color) 
it prints all the correct ones before and then stops on the invalid one"""

def draw_shape_from_string(turta):
    print("Enter a string on numbers from 0-9 and A, or press Enter to stop")
    user_input = input()
    while user_input:
        if not draw_line_from_string(user_input, turta):
            print(f"Invalid color found in string '{user_input}'. Stopping the drawing process.")
            break
        next_row(turta)
        print("Enter a string on numbers from 0-9 and A, or press Enter to stop")
        user_input= input()

#part 2  Danay

""" creates a checkerboard pattern, it loops through rows and cloumns adding 0 for even 
and 2 for odd ones. 0 is for black and 2 is for red. 
It draws the first line and then moves onto the next one till the checkerboard is completed"""

def  draw_grid(turta):
    checkerbaord = []
    for row in range(ROWS):
        line_num = ""
        for col in range(COLUMNS):
            if (row + col) % 2 == 0:
                line_num += '0'
            else:
                line_num += '2'
        draw_line_from_string(line_num, turta)
        next_row(turta)

#part 3 Naren
"""asks the user to first input the name of the file then it reads 
the content of the file and then prints the shape."""
def draw_shape_from_file(turta):
    filepath = input("Enter the location name of your file: ")
    f = open(filepath,"r")
    read =f.readlines()
    f.close()
    for i in read:
        i = i.strip()
        if i:
            draw_line_from_string(i, turta)
            next_row(turta)

def main():
    turta = Turtle()
    initialization(turta)
    draw_grid(turta)
    #draw_shape_from_string(turta)  
    #draw_shape_from_file(turta) 
    input("Press Enter to exit...")
# Main program execution
if __name__ == "__main__":
    main()