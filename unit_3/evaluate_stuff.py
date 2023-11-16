# evaluate my odb file: first image, then history output
# MP, 2023-11-16

from abaqus import *
from abaqusConstants import *
import numpy as np

odb_name = 'crack-model'

vp = session.viewports['Viewport: 1']

# open and view odb
odb = session.openOdb(name=odb_name+'.odb', readOnly=False)
vp.setValues(displayedObject=odb)

# got to the last frame (default)
vp.odbDisplay.setFrame(step=0, frame=-1)

# display the S22 contour plot
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))

vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT,
                                 refinement=(COMPONENT, 'S22'), )

# do not show all element edges
vp.odbDisplay.commonOptions.setValues(visibleEdges=FEATURE)

# hide stuff, adapt legend
vp.viewportAnnotationOptions.setValues(title=OFF, state=OFF, annotations=OFF, compass=OFF,triad=OFF)

vp.viewportAnnotationOptions.setValues(legendFont='-*-verdana-medium-r-normal-*-*-100-*-*-p-*-*-*')

vp.viewportAnnotationOptions.setValues(legendDecimalPlaces=3, legendNumberFormat=FIXED, 
                                       legendBackgroundStyle=MATCH)

# restore viewport, change size and position
vp.restore()
vp.setValues(width=130, height=90)
vp.setValues(origin=(13., 16.))

# manually dragged it so it looks nice: save view and load this view

session.View(name='User-1', nearPlane=24.058, farPlane=41.972, width=10.131, 
    height=6.9252, projection=PERSPECTIVE, cameraPosition=(4, 0, 33.015), 
    cameraUpVector=(0, 1, 0), cameraTarget=(4, 0, 0), viewOffsetX=-1.7003, 
    viewOffsetY=0.0031406, autoFit=OFF)

vp.view.setValues(session.views['User-1'])

# set options and print to file
session.pngOptions.setValues(imageSize=(1300, 900))

session.printOptions.setValues(vpDecorations=OFF, reduceColors=False)

session.printToFile(fileName=odb_name+'-s22_res', format=PNG, canvasObjects=(vp, ))