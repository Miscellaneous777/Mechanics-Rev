import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt # Import graphing based functions for Projectiles
matplotlib.use("TkAgg")
import numpy as np
from math import *

class projGraph():
    def __init__(self):
        self.gravity = 9.80665

    def makeGraph(self,f,vel,ang,final,time,high):
        t = np.linspace(0, time, 100)

        ang = radians(ang) #converting to radians

        xList = []
        yList = []

        for item in t: # For each time value
            xVal = vel*item*cos(ang) # Find a x-position
            yVal = vel*item*sin(ang) - 0.5*self.gravity*(item**2) # Find a y-position
            
            if yVal >= 0: # If y > or == 0, plot the point
                xList.append(xVal)
                yList.append(yVal)
            elif yVal < 0: # If y is negative, plot the final x point at y = 0.
                xList.append(final)
                yList.append(0)

        f.add_subplot(1,1,1)
                
        plt.plot(xList,yList) # Plot item

        if final > high: # if the x-axis is the larger axis
            axisThing = final # make both axis as long as the x-axis
        elif final < high: # if the y-axis is the larger axis
            axisThing = high # make both axis as long as the y-axis
        else: # if they're the same or something goes wrong
            axisThing = final # make em as wide as the x-axis

        plt.axis([0, axisThing+axisThing/20 , 0, axisThing+axisThing/20]) # change axis size
        
        #left='off', top='off', right='off', bottom='off', labeltop = 'off'
        #plt.show() # Show the graph

        return f

    def makeTeachGraph(self,l,vel,ang,final,time,high): # Had to copy this function due to a problem in the way MatPlotLib generates graphs - meaning that because I'd put it in one place it didn't want me to place it somewhere else.
        t = np.linspace(0, time, 100)

        ang = radians(ang) #converting to radians

        x1List = []
        y1List = []

        for item in t: # For each time value
            xVal = vel*item*cos(ang) # Find a x-position
            yVal = vel*item*sin(ang) - 0.5*self.gravity*(item**2) # Find a y-position
            
            if yVal >= 0: # If y > or == 0, plot the point
                x1List.append(xVal)
                y1List.append(yVal)
            elif yVal < 0: # If y is negative, plot the final x point at y = 0.
                x1List.append(final)
                y1List.append(0)

        print(y1List, x1List)

        l.add_subplot(1,1,1)
                
        #plt.plot(x1List,y1List) # Plot item
        plt.plot([1,2,3,4,5],[5,6,7,8,9])

        if final > high: # if the x-axis is the larger axis
            axisThing = final # make both axis as long as the x-axis
        elif final < high: # if the y-axis is the larger axis
            axisThing = high # make both axis as long as the y-axis
        else: # if they're the same or something goes wrong
            axisThing = final # make em as wide as the x-axis

        plt.axis([0, axisThing+axisThing/20 , 0, axisThing+axisThing/20]) # change axis size
        
        #left='off', top='off', right='off', bottom='off', labeltop = 'off'
        #plt.show() # Show the graph

        return l


if __name__ == "__main__":
    bobby = projGraph()
    f = plt.figure()
    bobby.makeGraph(f,40,72,95.9,73.8)
