# a small first Abaqus Python script
# MP, 2023-10-05

from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

# geometry parameters
w = 50
h = 15
ampl = 4
n_waves = 5

radius = 5.

# create x range from 0 to w with 100 points
x = np.linspace(0,w,100)
y = ampl * np.sin(n_waves*np.pi/w*x)

xy_points = np.column_stack((x,y))

Mdb()

# create sketch and draw lines and spline
s = mdb.models['Model-1'].ConstrainedSketch(name='my_sketch',
                                            sheetSize=200.0)

s.Line(point1=(0,-h), point2=(0,0))
s.Line(point1=(w,-h), point2=(w,0))
s.Line(point1=(0,-h), point2=(w,-h))
s.Spline(xy_points)

# creates png image out of sketch geometry
s.setPrimaryObject(option=STANDALONE)
session.printToFile(fileName='test', format=PNG, canvasObjects=(
                    session.viewports['Viewport: 1'],))

mdb.saveAs('test')