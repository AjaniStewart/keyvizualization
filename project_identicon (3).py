
# coding: utf-8

# # Identicon
# This program makes pretty pictures

# In[40]:

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.colors as clr
import random
import pylab
# input string 288 bits, convert to hexadecimal rep[x]
# output 12 * 12 grid, cells 4 different colors[x]
# mapping 00-> white , 01 -> light blue, ....[x]
# http://stackoverflow.com/questions/10194482/custom-matplotlib-plot-chess-board-like-table-with-colored-cells[x]
#make smaller subsection of the existing corners
#save them
#Show both plots at the same time!

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

def color_grid(grid):
    #determines color(White, light blue, blue, navy/dark blue) of each cell based on the string
    global zvals
    zvals = np.zeros(shape=(12,12))
    coded_string = string_to_bit("ce361f3f109a8e845e2b9bb3aaa025d3e9903239afd14ab4c90b93c39a8b8e9085c1a4gc5")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            zvals[i][j] = coded_string[i*12+j]
    cmap = clr.ListedColormap(['white', 'lightblue', 'blue', 'navy'])
    zvals[0][1] = 1
    bounds=[0,1,2,3,4]
    norm = clr.BoundaryNorm(bounds, cmap.N)
    grid = plt.imshow(zvals, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm)
    
# Make a 12x12 grid...
def draw_grid():
    #size of the image in inches(width,height) and dpi   
    plt.figure(figsize=(2,2), dpi = 113)
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
    #pylab.savefig("Original.png", bbox_inches ='tight')
    plt.show()
    
    
#New grid created with differences    
def draw_grid_altered():  
    plt.figure(figsize=(2,2), dpi = 113)
    nrows, ncols = 12, 12
    image = np.zeros(nrows*ncols)
    image = image.reshape((nrows, ncols))
    switch_color_top_left(color_grid(image))#change difference here
    frame = plt.gca()
    frame.set_frame_on(False)
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    #pylab.savefig("Switch_color_top_left.png", bbox_inches ='tight')
    plt.show()
    
    
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
    
#These functions switches colors of cells in the grid(white<-->lightblue, blue<-->navy)     
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
    
    
#Switches the colors of 2 random adjacent cells with each other(if cell 1 was white and cell 2 was blue, cell 2 will be )
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
    

def test1():
    draw_grid_altered()
    
    
def test2():
    draw_grid()
test1()
#test2()


# In[27]:

print ord("412"[0])-ord("0")


# In[118]:

13%4


# In[48]:

13/4


# In[11]:

len("ce361f3f109a8e845e2b9bb3aaa025d3e9903239afd14ab4c90b93c39a8b8e9085c")


# In[21]:

from matplotlib import pyplot as plt
plt.figure(figsize=(1,1))
x = [1,2,3]
plt.plot(x, x)
plt.show()


# In[36]:

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )


# In[ ]:



