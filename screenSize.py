import curses as crs
#Initialize screen
screen = crs.initscr()
#Set proper key settings
crs.noecho()
crs.cbreak()
screen.keypad(True)
#Do stuff
screen.addstr("This screen is " + str(crs.COLS) + " columns wide and " + str(crs.LINES) + " tall.\n")
while screen.getkey().upper() != 'X':
	screen.addstr("Press \'x\' to exit!\n")
#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
