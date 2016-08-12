import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.colors as clr
import random
#remove patterns!


def string_to_bit(text):
#converts the string(72 chars, 288 bits) into bits to determine the color of each cell
    out_array = []
    for i in range(len(text)):
        narray = [0,0]
        if ord(text[i].upper()) <= ord("9"):
            n = ord(text[i]) - ord("0")
        else:
            n = ord(text[i].upper()) - ord('A') + 10
        narray[1] = n%4
        narray[0] = n/4
        #print text[i], n
        out_array = out_array + narray
    return out_array

def color_grid(grid, cnum=None, rnum=None, color=None):
    #determines color(White, light blue, blue, navy/dark blue) of each cell based on the string
    global zvals
    zvals = np.zeros(shape=(12,12))
    coded_string = string_to_bit("ce361f3f109a8e845e2b9bb3aaa025d3e9903239afd14ab4c90b93c39a8b8e9085c1a4gc5")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            zvals[i][j] = coded_string[i*12+j]
    #updating the color of a specific cell(color is the index of the color in the colormap)
    if cnum is not None and rnum is not None and color is not None:
        zvals[cnum][rnum] = color
    #HTML color codes    
    cmap = clr.ListedColormap(['#ffffff', '#d5e6f3', '#2f99c9', '#2d5775'])
    bounds=[0,1,2,3,4]
    norm = clr.BoundaryNorm(bounds, cmap.N)
    grid = plt.imshow(zvals, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm)
    
def test_with_switch():
    image = np.zeros(shape=(12,12))
    plt.figure(figsize=(2,2), dpi=113)
    color_grid(image)
    i = 2
    j = 8
    zvals[i+1][j-1] = 1
    zvals[i+1][j] = 0
    zvals[i+1][j+1] = 2
    zvals[i+1][j+2] = 3
    zvals[i][j+2] = 0
    zvals[i-1][j+2] = 2
    zvals[i-1][j+1] = 1
    zvals[i-1][j] = 2
    zvals[i-1][j-1] = 3
    zvals[i][j-1] = 0
    zvals[i][j] = 0
    zvals[i][j+1] = 1
    frame = plt.gca()
    frame.set_frame_on(False)
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    print j, i
    plt.show()
    
    


# Making the 12x12 grid...
def draw_grid():
    #size of the image in inches(width,height) and dpi   
    plt.figure(figsize=(2,2), dpi=113)
    nrows, ncols = 12, 12
    #creates array of zeroes that is nrows by ncols
    image = np.zeros(nrows*ncols)
    # Reshape things into a 12x12 grid and colors it.
    image = image.reshape((nrows, ncols))
    #print image 
    color_grid(image)
    #removes axes and frame from figure
    frame = plt.gca()
    frame.set_frame_on(False)
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    plt.draw()
    
    
#New grid created with differences    
def draw_grid_altered():  
    plt.figure(figsize=(2,2), dpi=113)
    nrows, ncols = 12, 12
    image = np.zeros(nrows*ncols)
    image = image.reshape((nrows, ncols))
    switch_color_all(color_grid(image))
    frame = plt.gca()
    frame.set_frame_on(False)
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    plt.draw()
    
#These functions switches colors of cells in the grid(white<-->lightblue, blue<-->navy)  
def color_switch(i,j):
    if zvals[i][j] == 0:
        zvals[i][j] = 1
    elif zvals[i][j] == 1:
        zvals[i][j] = 0
    elif zvals[i][j] == 2:
        zvals[i][j] = 3
    else:
        zvals[i][j] = 2
    print j ,i
    
def switch_color_all(color_grid):
    for i in range(12):
        for j in range(12):
            color_switch(i,j)
    
def switch_color_top_left(color_grid):
#i = y axis, j = x-axis
    i =random.randint(6,11)
    j = random.randint(0,5)
    color_switch(i,j)
              
def switch_color_bot_left(color_grid):
    i = random.randint(0,5)
    j = random.randint(0,5)
    color_switch(i,j)
    
def switch_color_top_right(color_grid):
    i = random.randint(6,11)
    j = random.randint(6,11)
    color_switch(i,j)

def switch_color_bot_right(color_grid):
    i = random.randint(0,5)
    j = random.randint(6,11)
    color_switch(i,j)
    
def switch_color_middle(color_grid):
    i = random.randint(3,9)
    j = random.randint(3,9)
    color_switch(i,j)
    
def switch_color_top_edge(color_grid):
    i = 11
    j = random.randint(0,11)
    color_switch(i,j)

def switch_color_left_edge(color_grid):
    i = random.randint(0,11)
    j = 0
    color_switch(i,j)
    
def switch_color_bot_edge(color_grid):
    i = 0
    j = random.randint(0,11)
    color_switch(i,j)

def switch_color_right_edge(color_grid):
    i = random.randint(0,11)
    j = 11
    color_switch(i,j)
    
    
#Switches the colors of 2 random adjacent cells with each other
def switch_value(i,j):
    m = random.randint(0,3)
    if m == 0:
        if i == 11:
            i = 10
        s = 0
        s = zvals[i][j]
        zvals[i][j] = zvals[i+1][j]
        zvals[i+1][j] = s
    elif m == 1:
        if j == 11:
            j = 10
        s = 0
        s = zvals[i][j]
        zvals[i][j] = zvals[i][j+1]
        zvals[i][j+1] = s
    elif m == 2:
        if i == 0:
            i = 1
        s = 0
        s = zvals[i][j]
        zvals[i][j] = zvals[i-1][j]
        zvals[i-1][j] = s
    else:
        if j == 0:
            j = 1
        s = 0
        s = zvals[i][j]
        zvals[i][j] = zvals[i][j-1]
        zvals[i][j-1] = s
    print j,i
    
def switch_value_top_right(color_grid):
    i = random.randint(6,11)
    j = random.randint(6,11)
    switch_value(i,j)
    
def switch_value_bot_right(color_grid):
    i = random.randint(0,5)
    j = random.randint(6,11)
    switch_value(i,j)
    
def switch_value_top_left(color_grid):
    i =random.randint(6,11)
    j = random.randint(0,5)
    switch_value(i,j)
    
def switch_value_bot_left(color_grid):
    i = random.randint(0,5)
    j = random.randint(0,5)
    switch_value(i,j)
    
def switch_value_middle(color_grid):
    i = random.randint(3,9)
    j = random.randint(3,9)
    switch_value(i,j)

def switch_value_top_edge(color_grid):
    i = 11
    j = random.randint(0,11)
    switch_value(i,j)

def switch_value_left_edge(color_grid):
    i = random.randint(0,11)
    j = 0
    switch_value(i,j)
    
def switch_value_bot_edge(color_grid):
    i = 0
    j = random.randint(0,11)
    switch_value(i,j)
    
def switch_value_right_edge(color_grid):
    i = random.randint(0,11)
    j = 11
    switch_value(i,j)
    
    
def test1():
    draw_grid(), draw_grid_altered()
    plt.show()
    
