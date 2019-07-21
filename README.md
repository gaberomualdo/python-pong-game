# Python Pong

The classic pong game made in [Python Tkinter](https://docs.python.org/2/library/tkinter.html). Written for Python2 by [Fred Adams](https://xtrp.io/). Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
![Python Pong Graphic](graphic.jpg)

## Overview

The game is just like the original: the classic digital 2D table tennis game. Two-player and one-player (against AI) options are available.

The code is well commented, and only requires Python2 to be installed, however, it does use Tkinter, which should come pre-installed with Python2, but may not be for various reasons. Additional download information is below.

## Basic Instructions

In the two-player version, the first player (left paddle) uses the "W" and "S" keys to move up and down, respectively. The second player (right paddle) uses the up and down arrow keys to move up and down, respectively.

In the one-player version, the player is the left paddle, and uses the "W" and "S" keys to move up and down, respectively.

## Download and Play

1. Make sure you have Python installed. Install Python at [python.org](https://www.python.org/downloads/). Most computers running macOS should have Python pre-installed. Check if you have Python installed by typing the command ```python``` and pressing enter in your command prompt or terminal. If a prompt like ```>>>``` shows up, then Python is installed.

2. Python pong offers both two-player and one-player options: follow the directions accordingly for the option you choose.

    * **For two-player game:** Run the following command to download and play Python Pong two-player! Note that this will download a file called ```pong.py``` into your current working directory.

        ```bash
        curl https://xtrp.github.io/python-pong/pong_two_player.py -o pong.py && python pong.py
        ```

    * **For one-player game vs/AI:** Run the following command to download and play Python Pong one-player! Note that this will download a file called ```pong.py``` into your current working directory.

        ```bash
        curl https://xtrp.github.io/python-pong/pong_one_player.py -o pong.py && python pong.py
        ```

## One-Player AI Behind-the-Scenes

In the one player version, the AI (right paddle), uses the ```optimalPaddlePosition``` function to fetch the calculated projected position of where the ball will land. The AI then uses that data to move its paddle to hit the ball.

The ```optimalPaddlePosiiton``` function (calculates projected landing position of ball) works by using ball speed, position, and size to simulate the game and get the ball position at the exact point where it lands. It adds randomization to make the AI slightly imperfect (or else the AI would be unbeatable), and you can change this by editing the content of the ```if``` statement defined on line 225, or changing the condition of that same ```if``` statement. See comments within code for more details.

## Bugs or Issues

If you find a bug or have an issue with Python Pong, feel free to [Submit an Issue](https://github.com/xtrp/python-pong/issues/new).
