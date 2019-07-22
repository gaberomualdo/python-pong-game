# this program is written for Python2

# imports
import Tkinter
import time
import random
import sys
from copy import copy

# create game window
window = Tkinter.Tk()

# create window size and set no-resize option
window_dimensions = [800, 625]
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
player_y_velocity = 0

# ai variables
ai_y_position = initial_y_position
ai_y_velocity = 0

# ball variables
ball_diameter = 15

initial_ball_position = [(window_dimensions[0] - 35 - paddle_size[0]) - (int(window_dimensions[1] / 2)), ((window_dimensions[1] - ball_diameter) / 2) - (int(window_dimensions[1] / 2))]
initial_ball_velocity = [12, 12]

ball_position = copy(initial_ball_position)
ball_velocity = copy(initial_ball_velocity)

# score variable and widget
score = [0, 0]

# delete useless global variables
del initial_y_position

# display instructions variable
display_instructions = True

# optimal ai position
optimal_position = False

# gameloop
def gameloop():
	# declare use of global variables
	global frames_per_second
	global game_canvas
	global window_dimensions
	global player_y_position
	global paddle_size
	global ai_y_position
	global ball_diameter
	global ball_position
	global ball_velocity
	global player_y_velocity
	global ai_y_velocity
	global display_instructions
	global optimal_position

	# call gameloop again in 100 milleseconds (gameloops is called every 100 MS)
	window.after(1000 / frames_per_second, gameloop)

	# clear canvas
	game_canvas.delete("all")
	
	# create dark gray background
	game_canvas.create_rectangle(0, 0, window_dimensions[0], window_dimensions[1], fill="#222222", outline="#222222")

	# display player paddle (35 pixels from left)
	game_canvas.create_rectangle(35, player_y_position, 35 + paddle_size[0], player_y_position + paddle_size[1], fill="#ffffff", outline="#ffffff")

	# display ai paddle (35 pixels from right)
	game_canvas.create_rectangle(window_dimensions[0] - 35, ai_y_position, (window_dimensions[0] - 35) - paddle_size[0], ai_y_position + paddle_size[1], fill="#ffffff", outline="#ffffff")

	# display ball
	game_canvas.create_rectangle(ball_position[0], ball_position[1], ball_position[0] + ball_diameter, ball_position[1] + ball_diameter, fill="#ffffff", outline="#ffffff")

	# display score (centered)
	game_canvas.create_text(window_dimensions[0] / 2, 35, anchor="center", font="Monaco 28 bold", fill="#ffffff", text=str(score[0]) + "   " + str(score[1]))

	# display center separator line
	game_canvas.create_line((window_dimensions[0] / 2) , 0, (window_dimensions[0] / 2), window_dimensions[1], fill="#ffffff", dash=(6, 10), width=3)

	# display instructions
	if(display_instructions):
		game_canvas.create_text((window_dimensions[0] / 2) - 30, window_dimensions[1] - 40, anchor="ne", font="Monaco 16 bold", fill="#ffffff", text="Move w/WASD")

	# update player Y position and movement
	player_y_position += player_y_velocity

	# update ai Y position and movement
	ai_y_position += ai_y_velocity
	
	# set window boundaries for max and min position for paddles
	
	# player paddle
	if(player_y_position + paddle_size[1] > window_dimensions[1]):
		player_y_position = window_dimensions[1] - paddle_size[1]
	elif(player_y_position < 0):
		player_y_position = 0

	# ai paddle
	if(ai_y_position + paddle_size[1] > window_dimensions[1]):
		ai_y_position = window_dimensions[1] - paddle_size[1]
	elif(ai_y_position < 0):
		ai_y_position = 0

	# update ball position
	ball_position[0] += ball_velocity[0]
	ball_position[1] += ball_velocity[1]

	# set window boundaries for ball

	# top and bottom of screen
	if(ball_position[1] >= window_dimensions[1] - ball_diameter or ball_position[1] <= 0):
		ball_velocity[1] = -ball_velocity[1]

	# left side and right side of screen --> update score accordingly and reset ball vars
	if(ball_position[0] <= 0):
		# point for ai
		score[1] += 1
		
		# reset ball vars
		ball_position = copy(initial_ball_position)
		ball_velocity = copy(initial_ball_velocity)

		# reset optimal position var
		optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, paddle_size)

	if(ball_position[0] >= window_dimensions[0] - ball_diameter):
		# point for player
		score[0] += 1

		# reset ball vars
		ball_position = copy(initial_ball_position)
		ball_velocity = copy(initial_ball_velocity)

		# reset optimal position var
		optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, paddle_size)

	# paddle collision (also possibly one of the longest if statements you've seen in your life)
	if(((ball_position[0] >= 35 and ball_position[0] <= 35 + paddle_size[0]) and (ball_position[1] + ball_diameter >= player_y_position and ball_position[1] <= player_y_position + paddle_size[1]) and ball_velocity[0] <= 0) or ((ball_position[0] + ball_diameter <= window_dimensions[0] - 35 and ball_position[0] + ball_diameter >= (window_dimensions[0] - 35) - paddle_size[0]) and (ball_position[1] + ball_diameter >= ai_y_position and ball_position[1] <= ai_y_position + paddle_size[1]) and ball_velocity[0] >= 0)):
		ball_velocity[0] = -ball_velocity[0]

		# switch Y velocity if collision was on top or bottom sides of paddle

		# player paddle
		if(ball_velocity[0] >= 0):
			if((ball_position[1] + ball_diameter <= player_y_position + paddle_size[0] and ball_velocity[1] >= 0) or (ball_position[1] >= player_y_position + paddle_size[1] - paddle_size[0] and ball_velocity[1] <= 0)):
				ball_velocity[1] = -ball_velocity[1]

		# ai paddle
		if(ball_velocity[0] <= 0):
			if((ball_position[1] + ball_diameter <= ai_y_position + paddle_size[0] and ball_velocity[1] >= 0) or (ball_position[1] >= ai_y_position + paddle_size[1] - paddle_size[0] and ball_velocity[1] <= 0)):
				ball_velocity[1] = -ball_velocity[1]

		# update ai optimal position based on velocity change
		if(ball_velocity[0] <= 0):
			optimal_position = False
		else:
			optimal_position = optimalPaddlePosition(ball_velocity, ball_position, ball_diameter, paddle_size)

	
	# move ai according to function when ball is approaching
	if(ball_position[0] > window_dimensions[0] * 0.65):
		if(optimal_position != False and (ai_y_position < optimal_position and ai_y_position + paddle_size[1] > optimal_position)):
			ai_y_velocity = 0
		elif(optimal_position != False):
			if(ai_y_position > optimal_position):
				ai_y_velocity = -15
			if(ai_y_position < optimal_position):
				ai_y_velocity = 15


# ai optimal paddle position function
def optimalPaddlePosition(local_ball_velocity, local_ball_position, local_ball_diameter, local_paddle_size):
	# declare global variables
	global window_dimensions

	# reset arguments to set as values not pointers -- not passed by reference
	local_ball_velocity = copy(local_ball_velocity)
	local_ball_position = copy(local_ball_position)
	local_paddle_size = copy(local_paddle_size)

	
	# simulate ball movement until ball is at X-axis area where paddle is located
	while(local_ball_position[0] < window_dimensions[0] - 35 - local_paddle_size[0]):
		# update ball position
		local_ball_position[0] += local_ball_velocity[0]
		local_ball_position[1] += local_ball_velocity[1]

		# set top and bottom of screen boundaries
		if(local_ball_position[1] >= window_dimensions[1] - local_ball_diameter or local_ball_position[1] <= 0):
			local_ball_velocity[1] = -local_ball_velocity[1]
	
	# return paddle with location of ballafter simulation (optimal paddle position to hit ball), with a random number added 55% of the time to make ai imperfect
	local_optimal_position = local_ball_position[1]

	# add randomization 55% of the time
	if(random.randint(0, 100) <= 55):
		# add either -20 or 20 (randomly chosen) to optimal position variable
		local_optimal_position += [-20, 20][random.randint(0, 1)]
	
	# make sure optimal position variable is valid (position isn't within window boundaries)
	
	# bottom boundary
	if(local_optimal_position + local_ball_diameter > window_dimensions[1]):
		local_optimal_position = window_dimensions[1] - local_ball_diameter
	
	# top boundary
	if(local_optimal_position < 0):
		local_optimal_position = 0

	# return optimal position with added random value (already calculated in variable)
	return local_optimal_position

# handle arrow keys keydown events
def onKeyDown(e):
	# declare use of global variable(s)
	global player_y_velocity
	global ai_y_velocity
	global display_instructions

	# record current player velocities
	player_y_velocity_current = player_y_velocity
	ai_y_velocity_current = ai_y_velocity

	# bind arrow keys to player velocity changes
	if(e.keysym == "w"):
		# start movement up when up arrow is pressed down
		player_y_velocity = -15
	elif(e.keysym == "s"):
		# start movement down when down arrow is pressed down
		player_y_velocity = 15
	
	# turn off instructions if either paddle has moved
	if(player_y_velocity_current != player_y_velocity or ai_y_velocity_current != ai_y_velocity):
		display_instructions = False

# handle arrow keys keyup events
def onKeyUp(e):
	# declare use of global variable(s)
	global player_y_velocity
	global ai_y_velocity

	# bind arrow keys to player velocity change
	if(e.keysym == "w" or e.keysym == "s"):
		# stop movement when either arrow key is released
		player_y_velocity = 0

# connect keydown event to function
window.bind("<KeyPress>", onKeyDown)

# connect keyup event to function
window.bind("<KeyRelease>", onKeyUp)

# call gameloop
gameloop()

# display window and mainloop
window.mainloop()
