from pymel.core import *


def createJoints(selection = selected()):
	select(clear=True)

	for i in selection:
		joint()
		newJoint = ls(sl=1, o=1)
		matchTransform(newJoint, i)

createJoints()