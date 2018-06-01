import pymel.core as pm
from Qt import QtWidgets, QtCore, QtGui

class AutoRigUI(QtWidgets.QDialog):

    def __init__(self):
        super(AutoRigUI, self).__init__()
        self.setWindowTitle('TW Auto Rigger')
        self.setFixedSize(300,150)

        try:
            cmds.deleteUI('TW Auto Rigger')
        except:
            print('No other UI exists')

        self.buildUI()

    def buildUI(self):
        layout = QtWidgets.QGridLayout(self)

        guide_button = QtWidgets.QPushButton('Guides')
        guide_button.setFixedWidth(125)
        guide_button.setFixedHeight(25)
        guide_button.clicked.connect(self.rigAttr)
        layout.addWidget(guide_button, 1, 0)

        complete_button = QtWidgets.QPushButton('Complete')
        complete_button.setFixedWidth(125)
        complete_button.setFixedHeight(25)
        complete_button.clicked.connect(self.complete)
        layout.addWidget(complete_button, 1, 1)

    def rigAttr(self, s = pm.selected()):
        #creates attrubute on selected object /// Will check in the future if the selected object is a joint.
        if s.type == 'joint'
        pm.addAttr(attributeType='enum', longName='riggingAttribute', enumName='-----', keyable=True)
        pm.addAttr(attributeType='enum', longName='partOfBody', enumName='None:Arm:Leg:Spine:Hands', keyable=True)

    def complete(self, bodyPart=pm.getAttr('pm.ls(type="joint").partOfBody')):
        #Not working, but will use selceted body part to name the new joints properly.
        print('The part of the body selected is: %s' % bodyPart)


def showUI():
    ui = AutoRigUI()
    ui.show()
    return ui

################### Joint Creator #########################################

# Takes in a list of selected objs in the order the joints will be created.

def createJoints(selection=pm.selected()):
    pm.select(clear=True)
    for item in selection:
        pm.matchTransform(pm.joint(), item)
    pm.select(pm.selected()[0].root())
    alignJoints()


# recursive function that properly orinets all joints created using createJoints

def alignJoints():
    pm.selected()[0].orientJoint('xyz', sao='yup')
    try:
        pm.select(pm.listRelatives(children=True)[0])
        alignJoints()
    except:
        pm.joint(edit=True, orientation=(0, 0, 0))

#createJoints()
<<<<<<< HEAD
ui = showUI()
=======
buildUI()
>>>>>>> 65584eace7ca02cbc06781f669050b26dcabe51d
