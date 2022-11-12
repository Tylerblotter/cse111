# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from textwrap import fill
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    draw_cloud(canvas)
    draw_ground(canvas)
    draw_pine_trees(canvas)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas):
    draw_rectangle(canvas, 0,0, 800, 500, fill= 'skyblue')

def draw_cloud(canvas):
    draw_oval(canvas, 150, 400, 200, 350, fill= 'white', outline= 'white')
    draw_oval(canvas, 200, 400, 250, 350, fill= 'white', outline= 'white')
    draw_oval(canvas, 175, 425, 225, 375, fill= 'white', outline= 'white')
    draw_oval(canvas, 175, 375, 225, 325, fill= 'white', outline= 'white')
   
    draw_oval(canvas, 150, 400, 200, 350, fill= 'white', outline= 'white')

def draw_ground(canvas):
    draw_rectangle(canvas, 0, 0, 800, 100, fill= 'green', outline= 'green')
   

def draw_pine_trees(canvas):

    draw_rectangle(canvas, 300, 70, 320, 120, fill="brown")
    draw_polygon(canvas, 240, 110, 310, 320, 380, 110, fill="forestGreen")

    draw_rectangle(canvas, 200, 60, 220, 110, fill="brown")
    draw_polygon(canvas, 140, 100, 210, 310, 280, 100, fill="forestGreen")

    draw_rectangle(canvas, 100, 50, 120, 100, fill="brown")
    draw_polygon(canvas, 40, 90, 110, 300, 180, 90, fill="forestGreen")

   
    


# Call the main function so that
# this program will start executing.
main()