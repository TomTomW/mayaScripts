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


    def guideJoints(self):

        pm.select(pm.selected()[0].root())
        pm.select(hi=True)
        joints =  pm.selected()
        counter = 1
        for each in joints:
            pm.rename(each, 'guide_joint_' + str(counter))
            counter += 1

    def rigAttr(self):
        #creates attrubute on selected object /// Will check in the future if the selected object is a joint.

        #probably should only add Rig Attribute to parent???
        selected = pm.selected()
        if selected == []:
            print "please select joint"
        elif selected[0].nodeType() == 'joint':
            self.guideJoints()
            pm.addAttr(attributeType='enum', longName='riggingAttribute', enumName='-----', keyable=True)
            pm.addAttr(attributeType='enum', longName='partOfBody', enumName='None:Arm:Leg:Spine:Hands', keyable=True)
        else:
            print 'rigAttr() I am in the else statement'

        return pm.select(pm.selected()[0].root())




    def complete(self, bodyPart=pm.ls(type='joint')):
        '''
        #################################################
        In the future will only affect joints that are names with the prefix "guide"

        Will reference json file for proper names for completed joints.

        #################################################
        '''
        tempList = []
        for each in bodyPart:
            pm.select(each)
            tempList.append(pm.getAttr('.partOfBody'))
        print('The part of the body selected is: %s' % self.parts[tempList[0]])


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
