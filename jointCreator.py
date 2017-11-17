'''pesudo code

take in selection of locators

keep track of the number of locators that are selected

take in the number of selected items and loop on the number of them
matchTransform('what you want to move', 'object to move to') 

create a joint at each locatior'''
from pymel.core import *

class jointCreator:

	def createJoints(self, selection=selected()):
		select(clear=True)

		for i in selection:
			joint()
			newJoint = ls(sl=1, o=1)
			matchTransform(newJoint, i)

a = jointCreator()
a.createJoints()