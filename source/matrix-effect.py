import curses
import random
import time

def print_randomcharacter_stream(xc, yl, ws, variation=0):
    if variation == 1:
        char_stream = chr(random.randint(65,126))
        ws.addch(yl, xc, char_stream, curses.A_BOLD)
    elif variation == 2:
        ws.addch(yl, xc, ' ')
    else:
        char_stream = chr(random.randint(32,126))
        ws.addch(yl, xc, char_stream)
    ws.move(0,0)
    ws.refresh()

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.border()
    
    maxy, maxx = stdscr.getmaxyx()
    col_activated = [0] * (maxx - 2)
    flush_activated = [0] * (maxx - 2)
    generate_new = True
    
    while True:
        for xcol in range(maxx - 2):
            if col_activated[xcol] > 0:
                if col_activated[xcol] >= maxy - 1:
                    col_activated[xcol] = 1
                    generate_new = True
                if 51 <= flush_activated[xcol] <= 64:
                    print_randomcharacter_stream(xcol,col_activated[xcol],stdscr,2)
                elif 25 <= flush_activated[xcol] <= 50:
                    print_randomcharacter_stream(xcol,col_activated[xcol],stdscr,1)
                else:
                    print_randomcharacter_stream(xcol,col_activated[xcol],stdscr)
                flush_activated[xcol] += 1
                if flush_activated[xcol] > 65:
                    flush_activated[xcol] = 0
                col_activated[xcol] += 1
            if generate_new:
                new_col = random.randint(1,maxx - 3)
                col_activated[new_col] = 1
            generate_new = False

        action = stdscr.getch()
        if action == ord('q'):
            break
        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
