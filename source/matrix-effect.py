#!/usr/bin/env python

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
For a copy of the license see .
=====================================================================
Matrix Stream 
Sweeping of the screen surface and if column activated go for the next line
on that column print a random character (could be space or bold)
other possible options : curses.A_BLINK + curses.A_UNDERLINE + curses.A_STANDOUT
while opening a new column etc ...
=====================================================================
Friday, April 04, 2014
work (tested) with python 2.3 - 2.7 
www.peileppe.com

"""

import curses
import random
import time

def print_randomcharacter_stream(xc,yl,ws,variation=0):
    if variation==1:
        char_stream=chr(random.randint(65,126))
        ws.addch(yl,xc,char_stream, curses.A_BOLD)
    elif variation==2:
        ws.addch(yl,xc,' ')
    else:
        char_stream=chr(random.randint(32,126))
        ws.addch(yl,xc,char_stream)
    ws.move(0,0)
    ws.refresh()
    return

def main(self):
    w=curses.initscr()
    w.clear()
    w.border()
    w.keypad(1)
    w.nodelay(1)
    maxy, maxx =w.getmaxyx()
    
    action = ''
    col_activated=[0]*(maxx-2)
    flush_activated=[0]*(maxx-2)
    xcol=0
    generate_new=True
    
    while action != ord('q'):
        while xcol <= maxx-3:
            if col_activated[xcol] > 0:
                if col_activated[xcol] >= maxy-1:
                    col_activated[xcol]=1
                    generate_new=True
                if flush_activated[xcol] in range(51,65):
                    print_randomcharacter_stream(xcol,col_activated[xcol],w,2)
                elif flush_activated[xcol] in range(25,50):
                    print_randomcharacter_stream(xcol,col_activated[xcol],w,1)
                else:
                    print_randomcharacter_stream(xcol,col_activated[xcol],w)
                flush_activated[xcol]+=1
                if flush_activated[xcol] > 65:
                    flush_activated[xcol]=0
                col_activated[xcol]+=1
            if generate_new :
                new_col=random.randint(1,maxx-3)
                col_activated[new_col]=1
            xcol+=1
            generate_new=False
        xcol=0
        action=w.getch()
        time.sleep(0.1)
    curses.endwin()

if __name__ == '__main__':                                                       
	curses.wrapper(main)