import pymel.core as pm
from Qt import QtWidgets, QtCore, QtGui

class AutoRigUI(QtWidgets.QDialog):

    def __init__(self):
        super(AutoRigUI, self).__init__()
        self.setWindowTitle('TW Auto Rigger')
        self.setFixedSize(300,150)

        self.parts=['None', 'Arm', 'Leg', 'Spine', 'Hands']

        try:
            cmds.deleteUI('TW Auto Rigger')
        except:
            pass

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

        #probably should only add Rig Attribute to parent???
        guideJoints()
        if s[0].nodeType() == 'joint':
            pm.addAttr(attributeType='enum', longName='riggingAttribute', enumName='-----', keyable=True)
            pm.addAttr(attributeType='enum', longName='partOfBody', enumName='None:Arm:Leg:Spine:Hands', keyable=True)
        else:
            print "please select joint"

    def guideJoints(self, selected = pm.selected()):

        pm.select(hi=True)
        joints =  pm.selected()
        counter = 1
        for i in joints:
            pm.rename(i, 'guide_joint_' + str(counter))
            counter += 1

    def complete(self, bodyPart=pm.ls(type='joint')):
        '''
        #################################################
        Not working, but will use selceted body part to name the new joints properly. In the future
        will only affect joints that are names with the prefix "guide"

        Returns: Maya Attribute does not exist (or is not unique):: u'i.partOfBody'

        #################################################
        '''
        tempList = []
        for i in bodyPart:
            tempList.append(pm.getAttr('i.partOfBody'))
        print tempList
        #print('The part of the body selected is: %s' % self.parts[tempList[0]])


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
ui = showUI()