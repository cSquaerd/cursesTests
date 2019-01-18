import curses as crs

screen = crs.initscr()
crs.start_color()
crs.use_default_colors()
crs.noecho()
crs.cbreak()
crs.curs_set(0)

crs.init_color(1, 1000, 1000, 0)
crs.init_color(2, 0, 1000, 0)
crs.init_color(3, 1000, 0, 0)
crs.init_color(4, 1000, 750, 0)
crs.init_color(5, 0, 0, 1000)
crs.init_color(6, 500, 500, 1000)
crs.init_color(7, 1000, 500, 1000)
crs.init_pair(1, -1, 1)
crs.init_pair(2, -1, 2)
crs.init_pair(3, -1, 3)
crs.init_pair(4, -1, 4)
crs.init_pair(5, -1, 5)
crs.init_pair(6, -1, 6)
crs.init_pair(7, -1, 7)

screen.addstr("This is orange text!", crs.color_pair(4))
screen.addch(1, 0, 0x400000 + (crs.ACS_CKBOARD % 0x100))
screen.addstr(1, 2, "This cell's value is " + str(hex(screen.inch(1, 0))) + " / " + str(screen.inch(1, 0)))
for j in range(1, 8):
	screen.addch(j + 1, 0, 0x400000 + (crs.ACS_CKBOARD % 0x100), crs.color_pair(j))
	screen.addstr(j + 1, 2, "This cell's value is " + str(hex(screen.inch(j + 1, 0))) + " / " + str(screen.inch(j + 1, 0)) + " / " + str(hex(screen.inch(j + 1, 0) % 0x100)))
screen.getch()

crs.nocbreak()
crs.echo()
crs.endwin()
