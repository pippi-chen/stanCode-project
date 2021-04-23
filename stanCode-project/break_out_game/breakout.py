"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.ball_out_window():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.window.clear()
                graphics.end_lose()
                break

        graphics.ball.move(graphics._dx, graphics._dy)

        # Set of the situation that the ball touch the paddle.
        count_paddle = 0
        for i in range(2):
            for j in range(2):
                obj_paddle = graphics.window.get_object_at(graphics.ball.x + i * graphics.ball.width,
                                                           graphics.ball.y + j * graphics.ball.height)
                if obj_paddle == graphics.paddle:
                    count_paddle += 1
        if count_paddle > 0:
            graphics._dy = - graphics._dy

        # Set of the situation that the ball touch the brick.
        count_brick = 0
        for i in range(2):
            for j in range(2):
                obj_brick = graphics.window.get_object_at(graphics.ball.x + i * graphics.ball.width,
                                                          graphics.ball.y + j * graphics.ball.height)
                if graphics.ball.y < 240:
                    if obj_brick is not None:
                        count_brick += 1
                        graphics.window.remove(obj_brick)
                        graphics.score += 10
                        graphics.score_label.text = ('score: ' + str(graphics.score))
                        pass
        if count_brick > 0:
            graphics._dy = - graphics._dy

        # The situation that the coordinate of y of the ball is below the top of the window.
        if graphics.ball.y <= 5:
            graphics._dy = - graphics._dy

        # The situation that the coordinate of x of the ball is outside the window.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics._dx = - graphics._dx

        # The situation that the user wins the game.
        count_left_brick = 0
        for i in range(0, graphics.window.width, 45):
            for j in range(50, 240, 20):
                obj = graphics.window.get_object_at(i, j)
                if obj is not None:
                    count_left_brick += 1
        if count_left_brick == 0:
            graphics.window.clear()
            graphics.end_win()
            break






if __name__ == '__main__':
    main()
