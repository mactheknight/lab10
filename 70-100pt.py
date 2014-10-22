##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

line = drawpad.create_line(400,120,300,230)
line = drawpad.create_line(400,120,490,230)
rectangle = drawpad.create_rectangle(300,230,490,400)

rectangle = drawpad.create_rectangle(320,250,350,280)
rectangle = drawpad.create_rectangle(320,340,350,370)
rectangle = drawpad.create_rectangle(440,250,470,280)
rectangle = drawpad.create_rectangle(440,340,470,370)




root.mainloop()