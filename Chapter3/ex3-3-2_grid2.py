"""Andrea Cocco 2020
Chapter 3 Exercise 3-2 from the book:

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

2. Write a function that draws a similar grid with four rows and four columns. (See previous exercise)
"""

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_twice(f):
    f()
    f()

def plus_row():
    print('+','- '*4, end='')
    print('+','- '*4, end='')
    print('+','- '*4, end='')
    print('+', '- '*4,end='')
    print('+')

def pipe_row():
    print('|','  '*3,' |',end=' ')
    print('  '*3, ' |', end=' ')
    print('  '*3,' |',end=' ')
    print('  '*3, ' |')

def print_grid():
    plus_row()
    do_four(pipe_row)
    plus_row()
    do_four(pipe_row)

def print_four():
    do_twice(print_grid)
    plus_row()

print_four()
