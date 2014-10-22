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

# Creating outline of the house and roof
line = drawpad.create_line(400,120,300,230)
line = drawpad.create_line(400,120,490,230)
rectangle = drawpad.create_rectangle(300,230,490,400,fill='lavender')

# Creating the windows
rectangle = drawpad.create_rectangle(320,250,350,280,fill='white')
rectangle = drawpad.create_rectangle(320,340,350,370,fill='white')
rectangle = drawpad.create_rectangle(440,250,470,280,fill='white')
rectangle = drawpad.create_rectangle(440,340,470,370,fill='white')

# Creating the door and the chimney
rectangle = drawpad.create_rectangle(370,300,420,400,fill='lightblue')
line = drawpad.create_line(360,165,360,120)
line = drawpad.create_line(320,120,320,210)
line = drawpad.create_line(320,120,360,120)

# Creating lawn and door handle
rectangle = drawpad.create_rectangle(400,350,410,360,fill='grey')
rectangle = drawpad.create_rectangle(210,400,600,460,fill='lightgreen') 


root.mainloop()