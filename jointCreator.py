from pymel.core import *

# Takes in a list of selected objs in the order the joints will be created. 

def createJoints(selection = selected()):
	select(clear=True)

	for i in selection:
		joint()
		newJoint = ls(sl=1, o=1)
		matchTransform(newJoint, i)

createJoints()