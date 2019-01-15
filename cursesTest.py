import curses as crs
#Initialize screen
screen = crs.initscr()
#Set proper key settings
crs.noecho()
crs.cbreak()
screen.keypad(True)
#Do stuff
for i in range(10):
	screen.addstr(str(i) + " keys have been pressed...\t")
	screen.refresh()
	k = screen.getkey()
	try:
		screen.addstr(hex(ord(k)) + " was pressed!\n")
	except TypeError:
		screen.addstr("An arrow key was pressed!\n") #+ str(type(k)) + "\n")

while screen.getkey() != "x":
	screen.addstr("Hit the \'x\' key to exit!\n")

#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
