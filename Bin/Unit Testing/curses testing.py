import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the curses demo!")
    stdscr.addstr(1, 0, "Press 'q' to quit.")
    stdscr.addstr(2, 0, "Enter your name: ")
    stdscr.refresh()

    name = []
    x, y = 2, 13
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == 10:  # Enter key
            stdscr.addstr(3, 0, "Hello, " + ''.join(name) + "!")
            stdscr.refresh()
            break
        elif c == 127:  # Backspace key
            if name:
                name.pop()
                stdscr.addstr(y, x, ' ' * (len(name) + 1))
                stdscr.addstr(y, x, ''.join(name))
                stdscr.refresh()
        else:
            name.append(chr(c))
            stdscr.addstr(y, x, ''.join(name))
            stdscr.refresh()
            x += 1

curses.wrapper(main)