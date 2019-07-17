# this program is written for Python2

# imports
import Tkinter
import time
import random
import sys
import math

# create game window
window = Tkinter.Tk()

# create window size and set no-resize option
window_dimensions = [625, 625]
window.geometry(str(window_dimensions[0]) + "x" + str(window_dimensions[1]))
window.resizable(0, 0)

# set window title
window.title("Pong Game")

# close window when OS close button is clicked
window.protocol("WM_DELETE_WINDOW", sys.exit)

# choose fps for game
frames_per_second = 30

# create game canvas
game_canvas = Tkinter.Canvas(window, width=window_dimensions[0], height=window_dimensions[1], bd=0, highlightthickness=0)
game_canvas.pack()

# create game variables

# paddle sizes
paddle_size = [15, 125]

# initial centered Y position for both paddles
initial_y_position = (window_dimensions[1] - paddle_size[1]) / 2

# player variables
player_y_position = initial_y_position

# AI variables
ai_y_position = initial_y_position

# ball variables
ball_diameter = 15
ball_position = [(window_dimensions[0] - ball_diameter) / 2, (window_dimensions[1] - ball_diameter) / 2]

# delete useless global variables
del initial_y_position

# gameloop
def gameloop():
	# declare use of global variables
	global frames_per_second
	global game_canvas
	global window_dimensions

	# call gameloop again in 100 milleseconds (gameloops is called every 100 MS)
	window.after(1000 / frames_per_second, gameloop)

	# clear canvas
	game_canvas.delete("all")
	
	# create dark gray background
	game_canvas.create_rectangle(0, 0, window_dimensions[0], window_dimensions[1], fill="#222222", outline="#222222")

	# display player paddle (35 pixels from left)
	game_canvas.create_rectangle(35, player_y_position, 35 + paddle_size[0], player_y_position + paddle_size[1], fill="#ffffff", outline="#ffffff")

	# display AI paddle (35 pixels from right)
	game_canvas.create_rectangle(window_dimensions[0] - 35, ai_y_position, (window_dimensions[0] - 35) - paddle_size[0], player_y_position + paddle_size[1], fill="#ffffff", outline="#ffffff")

	# display ball
	game_canvas.create_rectangle(ball_position[0], ball_position[1], ball_position[0] + ball_diameter, ball_position[1] + ball_diameter, fill="#ffffff", outline="#ffffff")	

# handle arrow keys keydown events
def onKeyDown(e):
	# declare use of global variable(s)

	# bind arrow keys to specific player movements
	if(e.keysym == "Up"):
		pass
	elif(e.keysym == "Down"):
		pass
		

# connect keydown event to function
window.bind("<KeyPress>", onKeyDown)

# call gameloop
gameloop()

# display window and mainloop
window.mainloop()