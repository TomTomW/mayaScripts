import pymel.core as pm 

# Takes in a list of selected objs in the order the joints will be created. 

def createJoints(selection=pm.selected()):
	pm.select(clear=True)
    for item in selection:
        pm.matchTransform(pm.joint(), item)
    #parent = selected()[0].root()
    #orientJoint(parent)

createJoints()