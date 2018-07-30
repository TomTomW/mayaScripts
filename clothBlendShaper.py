####################################################
##### Written By: Nicolas Nixon and Tom Whitzer#####
####################################################

import pymel.core as pm
from Qt import QtWidgets, QtCore, QtGui

# User inter face for ease of use
# win = window(title="My Window")
# layout = columnLayout()
startFrame = x
lastFrame = y
iteration = z

##############
# Run if this is the FIRST range. Don't if it is the SECOND
pm.currentTime(0)
pm.duplicate('cloth_parent')
###############
pm.currentTime(startFrame)
currentTimeFramePos = pm.currentTime(query=True)
currentTimeFramePos = int(currentTimeFramePos)
###############
# Run if this is the First range. Don't if it is the SECOND
pm.rename('cloth_parent1' , 'cloth_parent_' + str(0))
###############
pm.currentTime(currentTimeFramePos)
###############
# If this is the SECOND range, comment out next line
list = []
while pm.currentTime(query=True) < lastFrame:
    pm.duplicate('cloth_parent')
    currentTimeFramePos = pm.currentTime(currentTimeFramePos + iteration)
    pm.currentTime(currentTimeFramePos)
    currentTimeFramePos = int(currentTimeFramePos)
    pm.rename('cloth_parent1', 'cloth_parent_' + str(currentTimeFramePos))
    list.append('cloth_parent_' + str(currentTimeFramePos))

print list
###############
#If this is the Second range, run first part on it's own, then change 'blendShape' number
pm.blendShape(list, 'cloth_parent_0')

pm.currentTime(startFrame)
newTimeFrame = pm.currentTime(query=True)
print ("newTimeFrame = " + str(newTimeFrame))
oldTimeFrame = pm.currentTime(startFrame - iteration)
print ("oldTimeFrame = " + str(oldTimeFrame))
futureTimeFrame = pm.currentTime(startFrame + iteration)
print ("futureTimeFrame = " + str(futureTimeFrame))
for each in list:
    pm.currentTime(newTimeFrame)
    pm.setKeyframe('blendShape1', attribute=each, t=oldTimeFrame, v=0)
    newTimeFrame = pm.currentTime(newTimeFrame + iteration)
    pm.setKeyframe('blendShape1', attribute=each, t=newTimeFrame, v=1)
    oldTimeFrame = pm.currentTime(newTimeFrame)
    futureTimeFrame = pm.currentTime(futureTimeFrame + iteration)
    pm.setKeyframe('blendShape1', attribute=each, t=futureTimeFrame, v=0)

##################################################
##################################################
##################################################

class clothWindow(object):

    def __init__(self):
        self.windowName = 'ClothBlendshaper'

    def show(self):

        window = pm.window(title=self.windowName, widthHeight=(400, 300))
        pm.columnLayout()
        pm.setParent('..')

        if pm.window(self.windowName, exists=True) == True:
            print ('I am in the if')
            pm.deleteUI(self.windowName)
            pm.showWindow()

        else:
            print ('I am in the else')
            pm.showWindow()


    def buildUI(self):





clothWindow().show()