'''
check box for fk/ik blend

text box for naming the joints.

name joints on creation.

function that adds IK/FK to two sets of copied joints
'''

import pymel.core as pm
from Qt import QtWidgets, QtCore, QtGui

def buildUI():


    layout = pm.window(title='Joint Creator', widthHeight=(250, 200))
    pm.columnLayout(adjustableColumn=True)
    pm.text(label='Part of body')
    pm.optionMenu()
    pm.menuItem(label='None')
    pm.menuItem(label='Arm')
    pm.menuItem(label='Leg')
    pm.text(label='Location')
    pm.optionMenu()
    pm.menuItem(label='L')
    pm.menuItem(label='M')
    pm.menuItem(label='R')
    pm.text(label='Name of Joints')
    jointName = pm.textField()
    blend = pm.checkBox(label='FK/IK Blend')
    pm.button(label='Create', command='createJoints()')
    pm.showWindow(layout)


def createJoints(selection=pm.selected()):
    pm.select(clear=True)
    for item in selection:
        pm.matchTransform(pm.joint(), item)
    pm.select(pm.selected()[0].root())
    alignJoints()
	
def alignJoints():
    pm.selected()[0].orientJoint('xyz', sao='yup')
    try:
        pm.select(pm.listRelatives(children=True)[0])
        alignJoints()
    except:
        pm.joint(edit=True, orientation=(0, 0, 0))

'''def copyJoints():
    pass'''

#createJoints()
buildUI()

'''testWin = pm.window(title = 'TempWin', widthHeight = (200, 55))
pm.columnLayout()
pm.button(label = 'nothing')
pm.button( label='Close', command=('pm.deleteUI(\"' + testWin + '\", window=True)')) 
#pm.setParent('..')
pm.showWindow(testWin)'''