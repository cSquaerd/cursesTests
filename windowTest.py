import curses as crs
#Initialize screen
screen = crs.initscr()
#Set proper key settings
crs.noecho()
crs.cbreak()
screen.keypad(True)
#Do stuff
window1 = crs.newwin(10, 20, 2, 5)
window1.addstr(1, 1, "This is Window 1")
window1.addstr(2, 1, "Hit \'x\' to exit")
for x in range(20):
	for y in (0, 9):
		if x == 19 and y == 9:
			window1.insch(y, x, "#")
		else:
			window1.addch(y, x, "#")
for x in (0, 19):
	for y in range(1, 9):
		window1.addch(y, x, "|")
window1.move(0, 0)
window1.refresh()

while window1.getkey().upper() != 'X':
	pass
#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
