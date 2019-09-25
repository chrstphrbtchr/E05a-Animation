#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade                           # Imports Python Arcade

SCREEN_WIDTH = 640                      # Sets width, height, and
SCREEN_HEIGHT = 480                     # title of the screen being
SCREEN_TITLE = "Move Keyboard Example"  # created.
MOVEMENT_SPEED = 3                      # Sets how fast the ball will move.


class Ball:                             # Creates the Ball class
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):  # defines what ball is

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x 
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):                     # Defines what to draw at the location from above
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)    # Draw the filled circle sprite
                                                                                                # from Python Arcade with the
                                                                                                # attributes listed (defined
                                                                                                # further below)

    def update(self):                   # Defines what update function does to self
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.TANGELO)       # Color of the background

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.PALE_CERULEAN)  # Color and parameters of the ball

    def on_draw(self):                                          # Defines on_draw function
        """ Called whenever we need to draw the window. """
        arcade.start_render()                                   # Rendering start
        self.ball.draw()                                        # Draw ball

    def update(self, delta_time):                               # Defines what to do when updating
        self.ball.update()                                      # Ball updates

    def on_key_press(self, key, modifiers):                     # Defines what happens when a key is pressed
        """ Called whenever the user presses a key. """         
        if key == arcade.key.LEFT:                              # If left key is pressed
            self.ball.change_x = -MOVEMENT_SPEED                # Ball goes left (negative) on x axis at movement speed
        elif key == arcade.key.RIGHT:                           # If right key is pressed
            self.ball.change_x = MOVEMENT_SPEED                 # Ball goes right on x axis at movement speed
        elif key == arcade.key.UP:                              # If up key is pressed
            self.ball.change_y = MOVEMENT_SPEED                 # Ball goes up on y axis at movement speed
        elif key == arcade.key.DOWN:                            # If down key is pressed
            self.ball.change_y = -MOVEMENT_SPEED                # Ball goes down (negative) on y axis at movement speed

    def on_key_release(self, key, modifiers):                   # Defines what happens when key is released
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:   # if left or right keys are released
            self.ball.change_x = 0                              # ball stops moving along x axis 
        elif key == arcade.key.UP or key == arcade.key.DOWN:    # if up or down keys are released
            self.ball.change_y = 0                              # ball stops moving along y axis


def main():                                                     # defines the program
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # sets the window size and title
    arcade.run()                                                # runs Python Arcade


if __name__ == "__main__":
    main()                                                      # runs the program