from pymel.core import *

# Takes in a list of selected objs in the order the joints will be created. 

def createJoints(selection=selected()):
    for item in selection:
        matchTransform(joint(), item)
    #parent = selected()[0].root()
    #orientJoint(parent)

createJoints()