"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius, height=ball_radius, x=(window_width / 2 - ball_radius),
                          y=(window_height / 2 - ball_radius))
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_ball)
        onmousemoved(self.hand_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(2):
                self.brick_x = 0 + i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + j * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=self.brick_x, y=self.brick_y)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.window.add(self.brick)
        for i in range(brick_rows):
            for j in range(2):
                self.brick_x = 0 + i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + (j + 2) * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=self.brick_x, y=self.brick_y)
                self.brick.filled = True
                self.brick.fill_color = 'orange'
                self.window.add(self.brick)
        for i in range(brick_rows):
            for j in range(2):
                self.brick_x = 0 + i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + (j + 4) * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=self.brick_x, y=self.brick_y)
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                self.window.add(self.brick)
        for i in range(brick_rows):
            for j in range(2):
                self.brick_x = 0 + i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + (j + 6) * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=self.brick_x, y=self.brick_y)
                self.brick.filled = True
                self.brick.fill_color = 'green'
                self.window.add(self.brick)
        for i in range(brick_rows):
            for j in range(2):
                self.brick_x = 0 + i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + (j + 8) * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=self.brick_x, y=self.brick_y)
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                self.window.add(self.brick)
        self.score = 0
        self.score_label = GLabel('score: ' + str(self.score))
        self.score_label.font = '-30'
        self.window.add(self.score_label, x=0, y=635)

    def hand_move(self, mouse):
        # Make the paddle move with the mouse, and avoid the paddle move outside the window.
        self.paddle.x = mouse.x - self.brick.width / 2
        self.paddle.y = self.paddle.y
        if mouse.x + self.paddle.width / 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if mouse.x - self.paddle.width / 2 < 0:
            self.paddle.x = 0

    def set_ball_velocity(self):
        # Set the velocity of the ball.
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx
        if random.random() > 0.5:
            self._dy = -self._dy

    def start_ball(self, event):
        # Make the ball start to move.
        if self._dx == 0 & self._dy == 0:
            self.set_ball_velocity()

    def set_ball_position(self):
        # Set the position of the ball when the game still doesn't start.
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

    def reset_ball(self):
        # As the user make the ball touch the bottom of the window, the ball will reset at the original position and
        # new velocity.
        self.set_ball_position()
        self.set_ball_velocity()

    def ball_out_window(self):
        # Set the situation when the ball touch the bottom of the window.
        is_die = (self.ball.y + self.ball.height) >= self.window.height
        return is_die

    def end_lose(self):
        # If the user loses the game, this display will happen.
        self.label = GLabel('You are a Loser~~~', x=20, y=self.window.height / 3)
        self.label.font = '-40'
        self.window.add(self.label)

    def end_win(self):
        # If the user wins the game, this display will happen.
        self.label = GLabel('You are a Winner~~~', x=0, y=self.window.height / 3)
        self.label.font = '-40'
        self.window.add(self.label)