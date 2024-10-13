#part 4 Rana
"""it imports the relevant functions from the pixart_start.py module and then execute them"""
from turtle import Turtle
from pixart_start import initialization, get_color, draw_color_pixel, draw_pixel, draw_line_from_string, next_row, draw_shape_from_string, draw_shape_from_file, draw_grid

def main():
    turta = Turtle()
    initialization(turta)
    draw_grid(turta)
    # draw_shape_from_string(turta)  
    # draw_shape_from_file(turta) 
    input("Press Enter to exit...")
# Main program execution
if __name__ == "__main__":
    main()