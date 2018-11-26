"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Brendan Boewe.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

boris = rg.SimpleTurtle()
boris.pen = rg.Pen('yellow',5)
boris.speed = 5

john = rg.SimpleTurtle()
john.pen = rg.Pen('blue', 1)
john.speed = 9

for k in range(5):
    boris.forward(100)
    boris.right(145)


john.pen_up()
john.left(90)
john.forward(100)
john.right(90)
john.forward(100)

for k in range(14):
    john.pen_down()
    john.right(120)
    john.forward(100)
    john.right(120)
    john.forward(100)
    john.right(120)
    john.forward(100)
    john.pen_up()
    john.right(25)


window.close_on_mouse_click()