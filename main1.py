#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade                                                       # Imports Python Arcade

SCREEN_WIDTH = 640                                                  # Sets screen width of window
SCREEN_HEIGHT = 480                                                 # Sets screen height of window
SCREEN_TITLE = "Move Mouse Example"                                 # Names the window / What the window will display


class Ball:                                                         # Beginning of the class "Ball"
    def __init__(self, position_x, position_y, radius, color):      # defines the class "Ball" and its parameters

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x                                # The position of x for ball is where x is for the mouse
        self.position_y = position_y                                # The position of y for ball is where y is for the mouse
        self.radius = radius                                        # The radius is the radius of ball
        self.color = color                                          # The color is the color of ball

    def draw(self):                                                 # Defines what to do when you draw the image
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)    # Draws a filled circle with the above
                                                                                                # attributes (which will be defined 
                                                                                                # further below)


class MyGame(arcade.Window):                                    # Beginning of MyGame class opening in the arcade window

    def __init__(self, width, height, title):                   # Defines the game

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.YELLOW_ORANGE)      # Determines the color of the background of the window

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.BLUE_VIOLET)       # Determines the size and color of the ball

    def on_draw(self):                                          
        """ Called whenever we need to draw the window. """
        arcade.start_render()                                   # Start of the game loop, begins arcade's rendering
        self.ball.draw()                                        # Creates the ball in the window

    def on_mouse_motion(self, x, y, dx, dy):                    # Defines what happens when the mouse moves in the window
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x                                # When mouse coordinates change, so do the ball's
        self.ball.position_y = y                                # When mouse coordinates change, so do the ball's

    def on_mouse_press(self, x, y, button, modifiers):          # Defines what happens when the mouse buttons get pressed
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")           # Prints this in the terminal (below)
        if button == arcade.MOUSE_BUTTON_LEFT:                  # If you click the left button...
            self.ball.color = arcade.color.PALE_CERULEAN                # ...the ball changes color!

    def on_mouse_release(self, x, y, button, modifiers):        # Defines what happens once the mouse button is released
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:                  # If you release the left button...
            self.ball.color = arcade.color.GENERIC_VIRIDIAN              # ... the ball color reverts! (or changes)


def main():                                                     # Defines the whole program
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # Opens the window upon running
    arcade.run()                                                # Runs arcade


if __name__ == "__main__":              
    main()                              # Runs the program