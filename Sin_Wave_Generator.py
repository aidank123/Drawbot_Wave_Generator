#DRAWBOT SIN WAVE GENERATOR V1

############################################

#IMPORTING MATH AND NUMPY MODULES
import math as m
import numpy as np
#import sys

#WIDTH OF TOTAL WINDOW VARIABLES -- Initial vals WIDTH = 500, HEIGHT = 500. 
    #Can be changed without breaking code

WIDTH = 100
HEIGHT = 100

#INITIALIZING WINDOW
size(WIDTH,HEIGHT)

#CREATING THE VARIABLE SLIDERS AND COLOR CHOOSER
    
Variable([
    
    #Amplitude of the sin wav (1 - HEIGHT/2)
    dict (name = "Amplitude", ui = "Slider",
    args=dict(
        value=1,
        minValue=1,
        maxValue=HEIGHT/2)),
       
   #Frequency of the sin wav (1 - 2)
   dict (name = "Frequency", ui = "Slider",
    args=dict(
        value=1,
        minValue=1,
        maxValue=2)),
        
    #Phase of the sin wav (0 - 10)
   dict (name = "Phase", ui = "Slider",
    args=dict(
        value=0,
        minValue=0,
        maxValue=10)),
        
    #Color of the line
    dict (name = "LineColor", ui = "ColorWell")
    
    ],globals())   	
        

#INITIALIZING ARRAY OF POINTS MAKING UP SIN WAV
points = []

pi = m.pi #initializing pi variable
numpoints = 100 #this variable can be increased for better resolution of the line, but this will creating buffering. Initialized to 100.
                
#ADDING POINTS IN WAV TO THE POINTS ARRAY
for x in np.arange(0,WIDTH,pi/numpoints):
     y = Amplitude * m.sin(Frequency * (x + Phase)) 
     points.append([x,y + HEIGHT/2])
     
#INITIALIZNG PATH
path = BezierPath()
path.moveTo(points[0]) #moving the path to the first point in the array

#CONNECTING ALL THE POINTS WITH arcTO from PATH
for i in range(len(points) - 1):
    path.arcTo(points[i],points[i + 1],0)
    
#Setting the color and width of the line with stroke(). The fill(None) assures the window will not fill in different colors on either side of the line. 
stroke(0,0,1,1)
stroke(LineColor) 
fill(None)

#Draw the path
drawPath(path)